# Auth & Conventions

Foundational reference for all pdf4me API operations: authentication, file encoding, parameter conventions, response formats, and error handling.

---

## Authentication

Every request requires the API key in the `Authorization` header using `Basic` authentication.

```
Authorization: Basic <your_api_key>
Content-Type: application/json
```

Store the key in an environment variable; never hardcode it:

```bash
export PDF4ME_API_KEY="your_api_key_here"
```

curl:

```bash
curl -X POST "https://api.pdf4me.com/api/v2/<ActionName>" \
  -H "Authorization: Basic $PDF4ME_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"docContent": "...", "docName": "file.pdf"}'
```

Python:

```python
headers = {
    "Authorization": f"Basic {os.environ['PDF4ME_API_KEY']}",
    "Content-Type": "application/json"
}
```

JavaScript (Node.js):

```javascript
const headers = {
  Authorization: `Basic ${process.env.PDF4ME_API_KEY}`,
  "Content-Type": "application/json",
};
```

---

## File Encoding Convention

All file content sent to — and received from — the API is **base64-encoded**.

**Encoding a file for upload:**

curl (bash):

```bash
DOC_CONTENT=$(base64 -w 0 document.docx)
```

Python:

```python
import base64

with open("document.docx", "rb") as f:
    doc_content = base64.b64encode(f.read()).decode("utf-8")
```

JavaScript (Node.js):

```javascript
const fs = require("fs");
const docContent = fs.readFileSync("document.docx").toString("base64");
```

**Decoding a file from the response:**

curl (bash, requires `jq`):

```bash
RESPONSE=$(curl -s -X POST "https://api.pdf4me.com/api/v2/<ActionName>" \
  -H "Authorization: Basic $PDF4ME_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"docContent\": \"$DOC_CONTENT\", \"docName\": \"document.docx\"}")

echo "$RESPONSE" | jq -r '."File Content"' | base64 -d > output.pdf
```

Python:

```python
result = response.json()
file_bytes = base64.b64decode(result["File Content"])
with open(result["File Name"], "wb") as f:
    f.write(file_bytes)
```

JavaScript (Node.js):

```javascript
const result = response.data;
const fileBytes = Buffer.from(result["File Content"], "base64");
fs.writeFileSync(result["File Name"], fileBytes);
```

---

## Parameter Key Convention (Critical)

The pdf4me docs display human-readable names in parameter tables but the **actual JSON payload keys are camelCase**. Two parameters are universal — present in every request:

| Docs display name | Actual JSON key |
| ----------------- | --------------- |
| File Content      | `docContent`    |
| File Name         | `docName`       |

Every operation also accepts its own set of additional parameters. Always check the **Payload** section of the specific endpoint in the pdf4me docs for the full list and their camelCase keys.

The **response** uses the display names as keys: `result["File Content"]`, `result["File Name"]`.

---

## Standard Response Format

Most endpoints return:

```json
{
  "File Content": "<base64-encoded file data>",
  "File Name": "output_filename.pdf"
}
```

Exceptions:

- **Split**: Returns `{"splited Documents": [...], "File Content": "...", "File Name": "..."}` (note: "splited" is the API's spelling)
- **Text extraction / OCR**: May return structured JSON with extracted text instead of a file

---

## Error Codes

| Code | Meaning           | Common cause                                                             |
| ---- | ----------------- | ------------------------------------------------------------------------ |
| 200  | Success           | —                                                                        |
| 400  | Bad Request       | Missing required parameter, wrong camelCase key, unsupported file format |
| 401  | Unauthorized      | Missing or invalid API key                                               |
| 403  | Forbidden         | Insufficient account permissions                                         |
| 404  | Not Found         | Incorrect endpoint name or path                                          |
| 429  | Too Many Requests | Rate limit exceeded — back off and retry                                 |
| 500  | Server Error      | Server-side issue — retry after a delay                                  |

Minimal error handling (Python):

```python
response = requests.post(url, headers=headers, json=payload)
try:
    response.raise_for_status()
except requests.HTTPError as e:
    print(f"HTTP {response.status_code}: {response.text}")
    raise
result = response.json()
```

Rate limit retry with exponential backoff:

```python
import time

for attempt in range(3):
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 429:
        time.sleep(2 ** attempt)
        continue
    response.raise_for_status()
    break
```

---

## Code Samples

### Python — complete example (ConvertToPdf)

See [`examples/convert-to-pdf.py`](../examples/convert-to-pdf.py).

Official samples for all operations across all supported languages:  
`https://github.com/pdf4me/pdf4me-api-samples`

Supported: **C# (.NET 6/8)**, **Java (8/11/21+)**, **Python (3.7+)**, **JavaScript (Node.js 14+)**, **Salesforce Apex**, n8n, Google Apps Script, AWS Lambda.
