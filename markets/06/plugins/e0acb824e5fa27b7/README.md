# EW Golden Baseline Model

<p align="center">
  <img src="assets/logo.jpg" alt="Embodied Worker logo／具象職人商標" width="320">
</p>

Natural-language algorithm selection and versioned time-series analysis Skills for Golden Baseline systems.

## English

### What this plugin does

EW Golden Baseline Model helps industrial users define deterministic time-series comparison methods without requiring them to understand or choose mathematical models.

It provides two Codex Skills:

- **Golden Baseline Algorithm Selector** — converts equipment, process, signal, event, and deviation requirements into a reusable policy using only backend-confirmed executable algorithm versions.
- **Golden Baseline Analysis Algorithm Builder** — creates, upgrades, or repairs a declarative and versioned analysis Skill with a machine-readable Manifest and normal, abnormal, and insufficient-data fixtures.

### Design principle

> Python computes deterministically, AI explains and configures, and engineers make the decision.

The plugin does not run arbitrary uploaded code and never self-certifies an algorithm as executable. It generates declarative candidates that must pass backend schema validation, Manifest compilation, fixed fixtures, version compatibility, and administrator approval.

### Typical workflow

1. Describe the equipment, process stages, signals, units, event markers, and comparison goal in plain language.
2. Let the selector choose the smallest suitable set from the backend's executable algorithm registry.
3. If a required capability is missing, use the builder to create or upgrade a candidate Skill with a Manifest and three fixture categories.
4. Upload the generated Markdown to the Golden Baseline Management System.
5. The backend validates the schema, compiles the Manifest, runs the fixtures, checks version compatibility, and returns actionable errors when revision is required.
6. Use the builder to repair failed candidates; only backend-passed and administrator-approved versions become executable.

### Included Skills

| Skill | Purpose |
|---|---|
| `golden-baseline-algorithm-selector` | Select only executable algorithm versions from process semantics and data conditions. |
| `baseline-analysis-builder` | Create, upgrade, or repair a declarative algorithm Skill with a Manifest and fixtures. |

### Safety boundary

- No EDC address, account, password, API key, SUID, or CUID is embedded in this repository.
- Generated Skills must not contain executable Python, SQL, Shell, JavaScript, credential access, or network operations.
- Generated algorithms do not become active merely because ChatGPT created them; the plugin cannot mark them executable.
- Production activation remains subject to backend validation and administrator approval.
- Algorithm results do not replace engineering approval for safety-critical decisions.

### Repository structure

```text
.
├── .codex-plugin/plugin.json
├── assets/logo.jpg
└── skills
    ├── golden-baseline-algorithm-selector
    │   ├── SKILL.md
    │   └── agents/openai.yaml
    └── baseline-analysis-builder
        ├── SKILL.md
        ├── agents/openai.yaml
        └── references
            ├── manifest-contract.md
            └── power-timeseries-example.md
```

### Installation

Install this repository as a Codex plugin using your approved local or organizational plugin marketplace workflow. Start a new Codex task after installation so the two Skills can be discovered.

### Copyright

Copyright © 2026 Embodied Worker Co., Ltd. All rights reserved.

---

## 中文

### 外掛用途

EW Golden Baseline Model 協助工業使用者定義確定性的時序比對方法，不要求使用者理解或自行選擇數學模型。

外掛包含兩個 Codex Skill：

- **黃金基線算法選擇**：把設備、工藝、訊號、事件與偏差需求，轉成只採用後端確認可執行版本的工藝政策。
- **時序分析算法建置、升級與修復**：建立、升級或依後端錯誤修復宣告式算法 Skill，並產生機器可讀 Manifest 及正常、異常、資料不足三類固定案例。

### 設計原則

> Python 負責確定性計算，AI 負責解釋與配置，工程師負責做決定。

此外掛不執行任意上傳程式碼，也不能自行宣告算法已可執行。它只產生宣告式候選規格；候選版本仍須通過後端格式驗證、Manifest 編譯、固定案例、版本相容及管理員核准。

### 標準使用流程

1. 使用自然語言描述設備、工藝階段、訊號、單位、事件錨點及比較目的。
2. 由算法選擇 Skill 從後端可執行算法登錄表判斷最小且適用的組合。
3. 如缺少能力，由建置 Skill 產生或升級包含 Manifest 與三類固定案例的候選算法。
4. 將生成的 Markdown 上傳至黃金基線管理系統。
5. 後端驗證格式、編譯 Manifest、執行固定案例、檢查版本相容；失敗時回傳可修復的錯誤。
6. 用建置 Skill 修復候選版本；只有後端通過並由管理員核准的版本才能成為可執行算法。

### 內含技能

| Skill | 用途 |
|---|---|
| `golden-baseline-algorithm-selector` | 依工藝語意與資料條件，只選擇已確認可執行的算法版本。 |
| `baseline-analysis-builder` | 建立、升級或修復包含 Manifest 與固定案例的宣告式算法 Skill。 |

### 安全邊界

- Repository 不包含 EDC 位址、帳號、密碼、API Key、SUID 或 CUID。
- 生成的 Skill 不得包含可執行的 Python、SQL、Shell、JavaScript、憑證存取或網路操作。
- ChatGPT 產生算法 Skill，不代表算法已經啟用；外掛不能自行標示為可執行。
- 正式啟用仍須通過後端驗證及管理員核准。
- 算法結果不能取代安全關鍵工作的工程師判斷。

### 安裝

請透過核准的本機或組織 Codex marketplace 流程安裝此 repository。安裝後開啟新的 Codex 工作階段，讓系統載入兩個技能。

### 版權

版權所有 © 2026 具象職人股份有限公司。保留所有權利。
