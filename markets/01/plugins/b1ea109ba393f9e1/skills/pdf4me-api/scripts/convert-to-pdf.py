import base64
import os

import requests


API_URL = "https://api.pdf4me.com/api/v2/ConvertToPdf"
HEADERS = {
    "Authorization": f"Basic {os.environ['PDF4ME_API_KEY']}",
    "Content-Type": "application/json",
}


def convert_to_pdf(input_path: str, output_path: str) -> None:
    with open(input_path, "rb") as file:
        doc_content = base64.b64encode(file.read()).decode("utf-8")

    payload = {
        "docContent": doc_content,
        "docName": os.path.basename(input_path),
    }

    response = requests.post(API_URL, json=payload, headers=HEADERS, timeout=120)
    response.raise_for_status()

    result = response.json()
    file_bytes = base64.b64decode(result["File Content"])

    with open(output_path, "wb") as file:
        file.write(file_bytes)
    print(f"Saved: {output_path}")


if __name__ == "__main__":
    convert_to_pdf("sample.docx", "output.pdf")
