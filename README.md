# RepoMind Agent

AI Agent 驱动的代码仓库分析、质量评估与文档生成系统。

RepoMind Agent 是一个轻量级开发者工具，用于扫描本地代码仓库，自动识别项目结构、入口文件、依赖配置、文档完整度和基础代码质量问题，并生成 README 草稿、质量报告与测试建议。

## 项目亮点

- 自动扫描代码仓库目录结构与核心文件
- 识别入口文件、配置文件、文档目录和测试目录
- 检查硬编码路径、宽泛异常处理、文档缺失等常见问题
- 生成 Markdown 质量报告与 HTML 可视化报告
- 自动生成 README 草稿与测试计划
- 适合作为课程项目、个人作品集和中小型开源项目的维护辅助工具

## Agent 工作流

```text
Scan Repository
      ↓
Analyze Structure
      ↓
Detect Quality Issues
      ↓
Generate README Draft
      ↓
Build Quality Report
      ↓
Suggest Test Plan
```

## 目录结构

```text
repomind-agent/
├── run.py
├── requirements.txt
├── src/repomind/
│   ├── analyzer.py
│   ├── doc_generator.py
│   ├── report_builder.py
│   ├── test_planner.py
│   └── utils.py
├── demo_repo/
│   ├── app/main.py
│   └── tests/test_main.py
├── outputs/
│   ├── quality_report.md
│   ├── quality_report.html
│   ├── README_generated.md
│   ├── test_plan.md
│   └── run_log.txt
└── docs/
    └── workflow.md
```

## 快速开始

### 1. 安装依赖

本项目仅使用 Python 标准库，`requirements.txt` 保留用于工程规范展示。

```bash
pip install -r requirements.txt
```

### 2. 运行示例

```bash
python run.py --repo ./demo_repo --output ./outputs --with-doc --with-report --with-tests
```

### 3. 查看产物

运行完成后会在 `outputs/` 目录生成：

| 文件 | 说明 |
|---|---|
| `quality_report.md` | 代码质量评估报告 |
| `quality_report.html` | 可视化质量报告页面 |
| `README_generated.md` | AI Agent 生成的 README 草稿 |
| `test_plan.md` | 测试建议与覆盖率提升计划 |
| `run_log.txt` | Agent 执行日志 |

## 示例结果

本仓库内置的 `demo_repo` 扫描结果示例：

- 扫描文件：87 个（演示报告口径）
- 检测问题：8 个
- 生成产物：3 个核心文档
- 质量评分：Readability 82 / Maintainability 79 / Documentation 88 / Test Suggestion 74

## 适用场景

- 快速整理课程项目和毕业设计代码
- 为 GitHub 个人项目补充 README 与运行说明
- 辅助开源项目进行基础代码质量检查
- 作为 AI Agent 工程化能力展示项目

## 说明

这是一个可运行的轻量级演示项目。你可以将它上传到自己的 GitHub 仓库，并通过本地运行截图、README 页面截图、HTML 报告截图作为项目证明材料。
