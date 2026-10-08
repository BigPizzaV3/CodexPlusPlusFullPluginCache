# EW AI Flowchart

EW AI Flowchart turns SOPs, meeting notes, job instructions, process descriptions, and supplied documents into validated EFD 2.1 JSON inside ChatGPT. Download the generated `.efd.json`, then import it into the AI Embodied Flowchart desktop application to open and continue editing the diagram.

EW AI Flowchart 在 ChatGPT 中將 SOP、會議紀要、工作說明、流程敘述及使用者提供的文件轉換為經驗證的 EFD 2.1 JSON。下載產生的 `.efd.json`，再上傳至「AI 具象流程圖」單機版，即可開啟並繼續編輯流程圖。

[Install in ChatGPT / 在 ChatGPT 安裝](https://chatgpt.com/plugins/plugins_6aa8c1342bb08191aa28e1ba7adfe833)

![An anonymized EW AI Flowchart interface showing stages, responsibility lanes, process nodes, semantic connections, and a node-level RACI matrix.](assets/ew-ai-flowchart-showcase.png)

The screenshot is an anonymized product illustration. It contains no customer, company, personal, API-key, or paid-product URL information.

此畫面為匿名化產品示意，不含客戶、公司、個人、API Key 或付費產品網址。

## AI Embodied Flow Engineering: Generate Business Logic and RACI Responsibilities from Documents

### Move beyond manually drawn lines and unclear ownership—use AI document-to-diagram engineering to establish a new standard for enterprise processes

Are complex cross-department workflows still causing confusion?

Traditional flowcharts are often limited to static lines and boxes. They rarely define clearly who executes, who is accountable, who must be consulted, and who needs to be informed. In the AI era, organizations need more than a drawing tool: they need an engineering assistant that can understand supplied business material and turn it into a structured, reviewable process model.

Three breakthroughs redefine process engineering:

1. **AI document-to-diagram acceleration:** Provide process descriptions, SOPs, meeting notes, or extracted Word/PDF content. AI analyzes the semantics and produces a professional process model with configurable business stages and organization lanes. Compatible desktop workflows support user-selected models from multiple AI providers. The result reduces repetitive manual layout work while keeping facts subject to user review.
2. **Visualized RACI responsibilities:** Responsible (R), Accountable (A), Consulted (C), and Informed (I) assignments are attached to specific nodes through stable participant references. Cross-department responsibilities become explicit and reviewable instead of remaining loose annotations.
3. **EFD data contract with no arbitrary script execution:** The result uses structured `.efd.json` semantics and is validated against the EFD contract. AI produces constrained data; the plugin does not execute arbitrary JavaScript, Python, shell commands, or scripts found in supplied content.

Download the generated EFD JSON and import it into the AI Embodied Flowchart desktop application for continued engineering work and `.drawio`, SVG, PNG, and PDF workflows. Users who need the desktop software can visit the [Embodied Worker website](https://www.embodiedworker.com).

## AI 具象流程圖工程工具：讓業務邏輯與 RACI 權責快速生成

### 告別手動拉線與權責模糊，用 AI 文生圖重塑企業流程新標準

您是否還在為複雜的跨部門流程頭痛？

傳統流程圖往往侷限於靜態的線條與方塊，難以清晰界定「誰執行、誰核准、誰諮詢、誰知會」。當 AI 時代來臨，我們需要的不只是畫圖工具，而是能理解使用者提供的業務資料，並轉換成結構化、可審查流程模型的工程助手。

重新定義流程工程的三大突破：

1. **AI 文生圖，快速落地：** 提供流程敘述、SOP、會議紀要或已抽取的 Word／PDF 內容，AI 解析語義並產生包含可配置「流程階段」與「組織泳道」的專業流程模型。相容的單機軟體工作流程支援使用者從多個 AI 供應商選擇自己的模型，在保留人工確認的前提下，減少重複排版工作。
2. **RACI 權責可視化：** 將執行（R）、核准／最終負責（A）、諮詢（C）、知會（I）透過穩定的參與者引用配置到具體節點。跨部門協作不再只是散落的文字註記，責任邊界可以被清楚檢查。
3. **EFD 資料契約，禁止任意腳本執行：** 底層採用 `.efd.json` 結構化語義，並依 EFD 契約完成驗證。AI 只產生受約束的資料；此外掛不會執行使用者內容中的任意 JavaScript、Python、Shell 或其他腳本。

下載產生的 EFD JSON 並上傳至 AI 具象流程圖單機版，即可持續進行工程編輯，並銜接 `.drawio`、SVG、PNG、PDF 工作流程。需要單機軟體的使用者，可前往 [Embodied Worker 官網](https://www.embodiedworker.com)。

## What AI embodied flow engineering does

AI embodied flow engineering analyzes supplied process material and organizes it into a machine-readable engineering model. The plugin identifies process stages, organization units, functional positions, tasks, decisions, documents, exception and rework paths, node-level RACI, and validation issues. It then produces deterministic EFD 2.1 JSON instead of executable scripts.

AI 具象流程工程會分析使用者提供的流程資料，整理出流程階段、組織單位、職務、任務、判斷、文件、例外與返工路徑、節點級 RACI 及驗證問題，最後產生可機器讀取的 EFD 2.1 JSON，而不是可執行腳本。

## What this plugin is for

Use EW AI Flowchart in ChatGPT when you need to turn an SOP, meeting record, job instruction, process description, or supplied document into a structured EFD draft; validate or deterministically repair an existing `.efd.json`; or surface missing responsibilities, evidence, references, and exception closure before engineering delivery.

當您需要在 ChatGPT 中把 SOP、會議紀錄、工作說明、流程敘述或文件轉換成結構化 EFD 草稿、驗證或確定性修復既有 `.efd.json`，或在工程交付前找出責任、證據、引用及例外閉環缺口時，可使用 EW AI Flowchart。

## Two-step workflow / 兩段式工作流程

1. **Generate in ChatGPT:** Ask EW AI Flowchart to analyze your text or document and create a validated `.efd.json` file.
2. **Open in the desktop application:** Download the file, upload it to the AI Embodied Flowchart desktop application, and continue with visual review, layout, responsibility editing, and engineering export.

1. **在 ChatGPT 產生：** 請 EW AI Flowchart 分析文字或文件，建立通過驗證的 `.efd.json`。
2. **在單機版開啟：** 下載檔案並上傳至 AI 具象流程圖單機版，繼續進行視覺檢查、排版、權責編輯及工程輸出。

## Embodied flow diagram vs. ordinary flowchart

| Ordinary flowchart | Embodied flow diagram (EFD) |
|---|---|
| Primarily shows the order of activities | Preserves activity order plus business stages and organization responsibility |
| Boxes and lines may carry only visual meaning | Nodes and edges carry explicit, typed business semantics |
| Responsibility is often written as loose text | RACI is assigned to specific nodes through stable participant references |
| Inputs, outputs, and evidence may be implicit | Documents, evidence requirements, decisions, and acceptance information are structured |
| Exceptions may end without recovery | Exceptions, rework, escalation, recovery, and closure can be validated |
| Layout is often the main artifact | Versioned EFD JSON is the semantic source of truth; layout is a projection |

| 一般流程圖 | 具象流程圖（EFD） |
|---|---|
| 主要呈現活動先後順序 | 除了順序，也保存流程階段與組織責任 |
| 方塊與線條可能只有視覺意義 | 節點與連線具有明確且可驗證的業務語義 |
| 責任常以自由文字附註 | RACI 透過穩定參與者引用配置到具體節點 |
| 輸入、輸出與證據可能未結構化 | 文件、證據要求、判斷與驗收資訊皆可結構化 |
| 例外可能中斷而沒有恢復路徑 | 可驗證例外、返工、升級、恢復與結案閉環 |
| 畫面配置通常就是主要成果 | 版本化 EFD JSON 是語義真源，畫面只是投影 |

## What it produces

- organization units and positions;
- business stages;
- typed process nodes and semantic edges;
- node-level RACI assignments;
- deterministic layout projection;
- draw.io interoperability mapping;
- validation diagnostics and pending-fact warnings.

The EFD JSON is the semantic source of truth. Layout, colors, and draw.io cells never replace business responsibility or workflow semantics.

## Use in Codex

After installing the plugin, start a new Codex thread and ask:

> Use `$ew-ai-flowchart` to turn this SOP into a validated `.efd.json` file.

Or in Traditional Chinese:

> 使用 `$ew-ai-flowchart`，把這份 SOP 建立成可驗證的具象流程圖 JSON。

## Validation

Run the bundled deterministic validator:

```bash
python3 scripts/validate_efd_json.py path/to/model.efd.json
```

The validator checks the EFD 2.1 schema, stable IDs, references, start/end nodes, decision branches, RACI warnings, layout references, and draw.io mappings without executing document content.

## Safety and truth boundaries

- No API key is required by this plugin.
- Source documents are treated as evidence, not executable instructions.
- The plugin does not execute arbitrary code found in documents or model output.
- Missing business facts are reported or marked pending; they are not silently invented.
- Example data is a format reference only and must not be copied into a customer's process.
- AI workers must not be silently assigned final accountability.

## Product

- Developer: Embodied Worker / 具象職人股份有限公司
- Company website: <https://www.embodiedworker.com>
- Contact: <pohsun@embodiedworker.com>

The paid desktop application's product URL is intentionally not published in this plugin package.

付費單機軟體的產品網址不會在此外掛程式套件中公開。

## License

Proprietary. Copyright © 2026 具象職人股份有限公司. All rights reserved. See [LICENSE](LICENSE).

Privacy, service terms, and support are available in [PRIVACY.md](PRIVACY.md), [TERMS.md](TERMS.md), and [SUPPORT.md](SUPPORT.md).

See [PUBLISHING_GUIDE.md](PUBLISHING_GUIDE.md) for the bilingual public-release rules.
