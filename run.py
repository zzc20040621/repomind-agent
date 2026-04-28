#!/usr/bin/env python3
"""Command line entry for RepoMind Agent."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from repomind.analyzer import RepositoryAnalyzer
from repomind.doc_generator import DocumentationGenerator
from repomind.report_builder import ReportBuilder
from repomind.test_planner import TestPlanner
from repomind.utils import ensure_dir, write_text


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="RepoMind Agent - repository analysis and documentation generator")
    parser.add_argument("--repo", required=True, help="Path to repository that should be analyzed")
    parser.add_argument("--output", default="./outputs", help="Output directory")
    parser.add_argument("--with-doc", action="store_true", help="Generate README draft")
    parser.add_argument("--with-report", action="store_true", help="Generate quality report")
    parser.add_argument("--with-tests", action="store_true", help="Generate test plan")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    repo_path = Path(args.repo).resolve()
    output_dir = ensure_dir(Path(args.output).resolve())
    log_lines: list[str] = []

    def log(level: str, message: str) -> None:
        line = f"[{level}] {message}"
        print(line)
        log_lines.append(line)

    log("INFO", "Starting RepoMind Agent workflow")
    log("INFO", f"Repository: {repo_path}")
    log("INFO", f"Output directory: {output_dir}")

    analyzer = RepositoryAnalyzer(repo_path)
    result = analyzer.run()

    log("INFO", f"Repository scan completed. files={result.total_files}, python_files={result.python_files}, markdown_files={result.markdown_files}")
    log("INFO", f"Entry point: {result.entry_file or 'not detected'}")
    log("INFO", f"Detected modules: {', '.join(result.core_modules[:5]) if result.core_modules else 'none'}")
    log("INFO", f"Detected issues: {len(result.issues)}")

    artifacts: list[str] = []

    if args.with_doc:
        doc_path = DocumentationGenerator(result).generate(output_dir)
        artifacts.append(str(doc_path.name))
        log("DONE", f"README draft generated: {doc_path}")

    if args.with_report:
        report_paths = ReportBuilder(result).generate(output_dir)
        artifacts.extend(path.name for path in report_paths)
        log("DONE", f"Quality report generated: {', '.join(path.name for path in report_paths)}")

    if args.with_tests:
        test_path = TestPlanner(result).generate(output_dir)
        artifacts.append(str(test_path.name))
        log("DONE", f"Test plan generated: {test_path}")

    log("DONE", f"RepoMind Agent completed successfully. artifacts={len(artifacts)}")
    write_text(output_dir / "run_log.txt", "\n".join(log_lines) + "\n")


if __name__ == "__main__":
    main()
