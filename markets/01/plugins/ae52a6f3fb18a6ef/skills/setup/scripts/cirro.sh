#!/bin/sh
set -eu

script_dir=$(CDPATH='' cd -- "$(dirname -- "$0")" && pwd)
version=$(sed -n '1p' "$script_dir/cirro-release.txt")
manifest_hash=$(sed -n '2p' "$script_dir/cirro-release.txt")
case "$(uname -s)" in
  Darwin) platform=macos; hash() { shasum -a 256 "$1" | cut -d ' ' -f 1; } ;;
  Linux) platform=linux; hash() { sha256sum "$1" | cut -d ' ' -f 1; } ;;
  *) echo "Cirro requires macOS or Linux; use cirro.cmd on Windows." >&2; exit 1 ;;
esac
machine=$(uname -m)
# A translated shell reports x86_64, and sandbox policies can block sysctl.
if [ "$platform" = macos ] && [ "$machine" = x86_64 ] &&
   [ "$(/usr/bin/arch -arm64 /usr/bin/uname -m 2>/dev/null || true)" = arm64 ]; then
  machine=arm64
fi
case "$machine" in
  x86_64|amd64) arch=x64 ;;
  arm64|aarch64) arch=arm64 ;;
  *) echo "Unsupported Cirro architecture: $(uname -m)" >&2; exit 1 ;;
esac
name="cirro-$platform-$arch"
cache="${DEMO_VIDEOS_CACHE:-$PWD/.demo-videos-cache}/$version"
mkdir -p "$cache"
cache=$(CDPATH='' cd -- "$cache" && pwd)
work=$(mktemp -d "$cache/run.XXXXXX")
trap 'rm -rf "$work"' EXIT
url="https://persistent.oaistatic.com/cirro/$version"

# Recheck cached archives and extract privately each time; never run a modified cached executable.
for file in SHA256SUMS "$name.zip"; do
  if [ ! -f "$cache/$file" ]; then
    curl --fail --silent --show-error --location --connect-timeout 15 --max-time 300 \
      --speed-limit 1024 --speed-time 30 --proto '=https' --proto-redir '=https' \
      "$url/$file" -o "$work/$file"
    mv "$work/$file" "$cache/$file"
  fi
  if [ "$file" = SHA256SUMS ]; then
    expected=$manifest_hash
  else
    expected=$(awk -v name="$file" '$2 == name {print $1}' "$cache/SHA256SUMS")
  fi
  if [ -z "$expected" ] || [ "$(hash "$cache/$file")" != "$expected" ]; then
    echo "Cirro checksum mismatch: $cache/$file. Remove that file and retry." >&2
    exit 1
  fi
done
unzip -q "$cache/$name.zip" -d "$work"
"$work/$name/cirro" "$@"
