#!/bin/sh
# Shared by bootstrap, command entrypoint and doctor; sourced, never executed.
skill_dir="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
version="${LEXMOUNT_BROWSER_CLI_VERSION:-1.2.1}"
case "$(uname -s)-$(uname -m)" in
  Darwin-arm64)
    target="aarch64-apple-darwin"
    default_install_dir="$skill_dir/bin"
    ;;
  Linux-x86_64)
    target="x86_64-unknown-linux-musl"
    # Plugin/config storage is not executable in ChatGPT Work.
    # Install dependencies in the normal user cache, never remount plugin storage.
    default_install_dir="${XDG_CACHE_HOME:-${HOME:?HOME is required}/.cache}/lexmount/browser-cli/$version/$target"
    ;;
  *) echo "Unsupported platform: $(uname -s) $(uname -m)" >&2; exit 2 ;;
esac
install_dir="${LEXMOUNT_BROWSER_CLI_INSTALL_DIR:-$default_install_dir}"
case "$install_dir" in /*) ;; *) echo "CLI install directory must be absolute" >&2; exit 2 ;; esac
binary="$install_dir/browser-cli"
