# Project document templates / 專案文件模板

Write every heading and field in the user's selected language. The English and Traditional Chinese labels below are semantic equivalents, not a requirement to duplicate both languages.

## PRODUCT.md

Include: project name / 專案名稱, one-sentence goal / 一句話目標, users / 使用者, current pain / 現況痛點, scenarios / 使用情境, inputs and outputs / 輸入輸出, workflow / 操作流程, screens / 主要畫面, MVP modules / MVP 模組, later phase / 第二階段, explicitly excluded / 明確不做, business rules / 商業規則, assumptions to confirm / 假設待確認, target platform and delivery artifact / 目標平台與交付成品, supported OS or device versions / 支援版本, installation and update expectations / 安裝與更新方式, success measures / 成功指標.

## ARCHITECTURE.md

Include: architecture goals and principles / 架構目標與原則, system boundary / 系統邊界, frontend, backend, modules, data model / 資料模型, file storage / 檔案保存, accounts and roles / 帳號角色, workspace isolation / 工作空間隔離, AI versus deterministic responsibilities / AI 與非 AI 分工, model routing / 模型路由, secrets / 密鑰, privacy / 隱私, logs / 日誌, target runtime and CPU architecture / 目標執行環境與處理器架構, build and packaging / 建置與打包, code signing, notarization, certificates, and store distribution when applicable / 適用時的簽章、公證、憑證與商店發佈, installation, update, and uninstall / 安裝更新與卸載, deployment / 部署, backup and rollback / 備份回滾, rationale / 技術選擇理由, risks and open decisions / 風險與待決定.

## ACCEPTANCE.md

Include scope, target operating system or device, required artifact type, environment, test data, and functional/error/boundary cases. When an installable or deployable artifact is required, include evidence-based cases for clean build, package creation, installation on the real target, first launch, upgrade without unintended data loss, rollback where applicable, and uninstall or service removal. Add authorization, privacy, performance, cost, backup, and rollback when applicable. Use the selected-language equivalent of:

```markdown
### AC-001 Case name / 案例名稱
- Related module / 對應模組：
- Given / 給定：
- When / 當：
- Then / 那麼：
- Must not / 不允許：
- Test data / 測試資料：
- Evidence / 驗收證據：
- Result / 結果：Not tested / 未測試
```

## AGENTS.md

Keep it concise. Include required reading, project purpose and scope, target platform and required delivery artifact, project map, build, test, and packaging commands, engineering and safety rules, smallest vertical slice, definition of done, and mandatory stop conditions. Mark unverified commands as `To confirm` / `待確認`; never invent them.

## START_CODEX.md

Use the user's selected language. The meaning must remain:

```markdown
# Start Codex implementation / 啟動 Codex 施工

Read PRODUCT.md, ARCHITECTURE.md, ACCEPTANCE.md, AGENTS.md, and the existing project completely.

In the first turn only:
1. Restate the goal, MVP, and excluded scope.
2. List open questions, assumptions, and major risks.
3. Inspect existing files, target platform, runtime, build toolchain, signing requirements, and available commands.
4. Propose the smallest vertical-slice plan.
5. List planned file changes, expected build/package artifacts, and acceptance cases.

Do not modify code in this turn. Wait for approval of the plan before implementation.
```

After plan approval, `START_CODEX.md` must also instruct Codex to:

- work in inspectable milestones rather than promise a completion time;
- build the smallest runnable vertical slice first;
- run documented checks and record actual results;
- create or update `PROJECT_STATUS.md` after each meaningful milestone;
- save recoverable GitHub milestones only when repository access and writes are authorized;
- stop for product-changing decisions, credentials, paid services, sensitive-data use, destructive operations, or release/public-access authorization;
- finish with the current build artifact, test evidence, failed or untested acceptance cases, preview instructions, known limitations, and the next action;
- tell the user to invoke EW AI Coding again with the project, repository, or Codex summary to continue testing, preview, acceptance, release, and value verification.
