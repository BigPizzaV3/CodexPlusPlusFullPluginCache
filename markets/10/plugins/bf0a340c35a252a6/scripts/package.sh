#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ARCHIVE="${ROOT}/../pretture-ai-chatgpt-plugin.zip"

python3 "${ROOT}/scripts/validate_package.py"
rm -f "${ARCHIVE}"
(
  cd "${ROOT}"
  zip -r "${ARCHIVE}" . \
    -x "*.DS_Store" \
    -x "__MACOSX/*" \
    -x "pretture-ai-chatgpt-plugin.zip"
)

echo "Created ${ARCHIVE}"
