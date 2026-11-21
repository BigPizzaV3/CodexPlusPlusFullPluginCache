# Install Tesseract graphics CLI 0.3.1

Pinned version: **0.3.1**. Public release: https://github.com/mirage-hq/tesseract/releases/tag/v0.3.1

Detect the actual host before selecting the bundle:
- macOS: use `uname -s` and `uname -m`. Use `darwin-arm64` on Apple Silicon, including when `sysctl -in sysctl.proc_translated` returns 1 under Rosetta; otherwise `darwin-x86_64` for Intel.
- Windows: use `windows-x86_64` only for AMD64 Windows 10+. Check PROCESSOR_ARCHITEW6432 when present, otherwise PROCESSOR_ARCHITECTURE.
- Linux: use `linux-x86_64` only on x86_64 with glibc 2.35+. Python 3, bash, coreutils, and unzip are required for installation. Runtime also needs zlib, ALSA, libstdc++, Vulkan loader and a compatible driver (Mesa lavapipe can provide software rendering).
- Stop on unsupported hosts; do not guess another archive.

Download both files to a fresh temporary directory, using curl -fL or Invoke-WebRequest:
`https://github.com/mirage-hq/tesseract/releases/download/v0.3.1/tesseract-0.3.1-<platform>.zip`
`https://github.com/mirage-hq/tesseract/releases/download/v0.3.1/tesseract-0.3.1-<platform>.zip.sha256`

Replace <platform> with the exact detected suffix above. GitHub login, Homebrew, Node, and administrator installation are not required. On unavailable assets or download errors, report the exact URL/error; do not substitute latest or a private build.

Verify before extraction or execution:
- macOS: run `shasum -a 256 -c <archive>.zip.sha256` from the download directory. Extract with `ditto -x -k <archive>.zip <new-extract-directory>`. Locate the extracted CLI folder and run `bash <extracted-folder>/install.sh "$HOME/Library/Application Support/TokenTally/Tesseract"`. This dedicated prefix preserves the user’s other Tesseract installation. The command is then `~/Library/Application Support/TokenTally/Tesseract/bin/tsrct`.
- Linux: run `sha256sum -c <archive>.zip.sha256`, extract with unzip into a fresh directory, and run the extracted `install.sh` with bash.
- Windows: compare Get-FileHash SHA256 with the checksum file, extract with Expand-Archive, and run the extracted install.ps1 using PowerShell. Follow local script execution policy and host approvals.

Stop if hashes differ. The installer also validates platform and bundle checksums. Run the installed command with `--version` and require 0.3.1 before rendering. Pass its absolute path with --tsrct.

Never bypass Gatekeeper, SmartScreen, organizational restrictions, or delete quarantine attributes. If installation or rendering is blocked, retain existing artifacts and report the actual error. Do not enable telemetry on the user's behalf. This installation guide is based on the Tesseract 0.3.1 plugin's public CLI installation workflow.
