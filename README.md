# HonestApply

HonestApply is a local-first job-fit screening foundation for truthful job
applications. It compares a structured candidate profile with a job and the
candidate's preferences, then explains whether the role is worth applying for.

HonestApply 是一个本地优先、强调真实性的职位匹配工具。它会比较候选人资料、
岗位要求和求职偏好，并说明是否建议申请以及不匹配的原因。

> **Current scope / 当前范围:** v0.2 provides an installable Codex Skill and
> screens structured JSON or YAML data. It does not yet generate resumes, scrape
> job websites, log in to job platforms, or submit applications. Those
> capabilities are roadmap items and must preserve human approval before
> submission.

## Features / 已实现功能

- Experience, English level, verified-claim, work-mode, and role-exclusion checks
- Explicit blocking of restricted or conflicting candidate claims
- Readable input errors for missing files, malformed YAML, missing fields, and invalid values
- Custom candidate, job, and preference files through command-line options
- Local processing; real private files do not need to be committed to Git
- Eight automated tests covering positive, negative, validation, truth-safety, and Skill entrypoint cases
- GitHub Actions test workflow

中文概览：

- 检查经验、英语等级、已核实经历、办公方式和排除岗位
- 明确阻止使用受限制经历，避免同一经历既“已核实”又“受限制”
- 对缺失文件、YAML 错误、缺少字段和无效值提供清晰提示
- 支持通过命令行指定不同用户的候选人、岗位和偏好文件
- 本地处理资料；真实隐私文件无需提交到 Git
- 提供 7 项自动测试和 GitHub 自动测试流程

## Core principles / 核心原则

- Truthful claims only / 只使用真实、可核实的经历
- Privacy-first local data / 隐私资料优先保存在本地
- Human approval before submission / 投递前必须由用户确认
- No blind mass applications / 不进行盲目海投
- Explain every recommendation / 每个建议都应提供原因

## Install as a Codex Skill / 安装为 Codex Skill

HonestApply can be installed as a Skill so nontechnical users can provide a
resume and job description in natural language without manually editing YAML.

Ask Codex to use its skill installer:

```text
Use $skill-installer to install the skill from:
https://github.com/industrial-product-ai/honest-apply
```

For a private repository, the tester must first be invited to the repository and
their environment must have authenticated GitHub access. After installation,
start a new task and try:

```text
Use $honest-apply to compare my resume with this job. Treat attachments as source
material, do not invent qualifications, and ask before sending anything externally.
```

The Skill keeps JSON/YAML preparation and deterministic matching in the
background. Users should not be asked to edit structured files unless they want
to inspect or customize them.

## Quick start on Windows / Windows 快速开始

Requirements: Git and Python 3.12 or newer.

```powershell
git clone https://github.com/industrial-product-ai/honest-apply.git
cd honest-apply
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Run the included examples / 运行内置示例：

```powershell
.\.venv\Scripts\python.exe app\main.py
```

Show command help / 查看命令帮助：

```powershell
.\.venv\Scripts\python.exe app\main.py --help
```

Use custom files / 使用自定义文件：

```powershell
.\.venv\Scripts\python.exe app\main.py `
  --candidate data\private\candidate.yaml `
  --job data\private\job.yaml `
  --preferences data\private\preferences.yaml
```

PowerShell uses the backtick at the end of a line to continue a command. You can
also place the entire command on one line.

## Input model / 输入资料

Start by copying these fictional files and editing the copies:

- `examples/candidate.example.yaml`
- `examples/job.example.yaml`
- `examples/preferences.example.yaml`

Recommended location for real data:

```text
data/private/
```

That directory is ignored by Git. Never replace the public example files with a
real person's resume, contact details, passwords, browser profile, or application
history.

### Truth model / 真实性模型

- `verified_claims`: facts the candidate can support and the matcher may use
- `restricted_claims`: unverified, exaggerated, sensitive, or prohibited claims
- A claim cannot appear in both lists
- If a job requires a restricted claim, HonestApply rejects the match

`verified_claims` 表示可以证明并允许使用的经历；`restricted_claims` 表示未经核实、
夸大、敏感或禁止使用的内容。同一经历不能同时存在于两个列表中。

## Run tests / 运行测试

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

A successful run ends with:

```text
Ran 8 tests
OK
```

## Project structure / 项目结构

```text
SKILL.md            Codex Skill workflow and safeguards / Skill 工作流与安全规则
agents/             Skill interface metadata / Skill 界面信息
app/
  main.py          Command-line interface / 命令行入口
  matcher.py       Matching and truth-safety rules / 匹配与真实性规则
  validation.py    Input validation / 输入验证
examples/          Fictional public YAML examples / 虚构公开示例
references/        Agent-only input schema / 智能体输入规范
scripts/           Dependency-free JSON entrypoint / 无外部依赖的 JSON 入口
tests/             Automated tests / 自动测试
```

## Roadmap / 后续计划

- v0.3: JSON report export and weighted preference scoring
- v0.4: evidence-linked, truthful resume tailoring drafts
- v0.5: local application tracker and approval records
- Later: browser-assisted form filling with explicit human approval before submission

## Security and privacy / 安全与隐私

Do not commit real resumes, contact information, API keys, passwords, cookies, or
browser profiles. Review `git status` before every commit. HonestApply v0.2 does
not connect to job platforms and never submits an application.

## License / 许可证

HonestApply is available under the [MIT License](LICENSE). You may use, modify,
and distribute it, including commercially, provided that the copyright and
license notice are retained. The software is provided without warranty.

HonestApply 采用 [MIT License](LICENSE)。在保留版权与许可证声明的前提下，
可以使用、修改、分发及商业使用；软件按现状提供，不包含任何担保。
