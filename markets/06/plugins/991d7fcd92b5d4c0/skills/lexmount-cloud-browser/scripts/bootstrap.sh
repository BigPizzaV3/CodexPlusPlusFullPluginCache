#!/bin/sh
set -eu

umask 077
. "$(dirname -- "$0")/runtime.sh"
download_base_url="${LEXMOUNT_BROWSER_CLI_DOWNLOAD_BASE_URL:-https://cli-bin-1377899528.cos.ap-nanjing.myqcloud.com/releases/browser-cli}"
repo="${download_base_url%/}/v${version}"

asset="browser-cli-v${version}-${target}"
tmp_dir="$(mktemp -d)"
trap 'rm -rf "$tmp_dir"' EXIT INT TERM
curl --proto '=https' --tlsv1.2 -fsSL "$repo/$asset" -o "$tmp_dir/$asset"
curl --proto '=https' --tlsv1.2 -fsSL "$repo/SHA256SUMS" -o "$tmp_dir/SHA256SUMS"
expected="$(awk -v name="$asset" '$2 == name {print $1}' "$tmp_dir/SHA256SUMS")"
[ -n "$expected" ] || { echo "No checksum published for $asset" >&2; exit 3; }
if command -v sha256sum >/dev/null 2>&1; then
  actual="$(sha256sum "$tmp_dir/$asset" | awk '{print $1}')"
elif command -v openssl >/dev/null 2>&1; then
  actual="$(openssl dgst -sha256 "$tmp_dir/$asset" | awk '{print $NF}')"
else
  echo "Neither sha256sum nor openssl is available for SHA-256 verification" >&2
  exit 5
fi
[ "$expected" = "$actual" ] || { echo "SHA-256 mismatch for $asset" >&2; exit 4; }
mkdir -p "$install_dir"
if [ -L "$binary" ]; then
  echo "Refusing to replace a symlink at CLI destination" >&2
  exit 5
fi
# Validate in the selected runtime directory before replacing an existing binary.
# An execution denial is final: no remount, alternate loader or fallback copy.
staged="$(mktemp "$install_dir/.browser-cli.XXXXXX")"
trap 'rm -rf "$tmp_dir"; rm -f "$staged"' EXIT INT TERM
cp "$tmp_dir/$asset" "$staged"
chmod 0755 "$staged"
"$staged" version
mv -f "$staged" "$binary"
echo "Installed browser-cli to $binary"
