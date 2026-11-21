---
name: darling-runtime
description: Use when the user wants to install, inspect, troubleshoot, or run macOS Mach-O command-line tools or compilers with the bundled Darling runtime on compatible Linux hosts.
---

# Darling Runtime

This skill ships official Darling v0.1.20260608 release-era Ubuntu Noble amd64 binary packages inside `assets/binaries/`.

## Scope

Prefer CLI and compiler workloads. Explain that Darling is a compatibility layer, not macOS and not a VM. GUI support is included where practical but is secondary.

## Host assumptions

The bundled DEBs target Ubuntu 24.04 (Noble), amd64. Do not attempt to install them on another architecture. Before installation, inspect the host OS and architecture.

## Install

Use `assets/install.sh` from this skill directory when local execution is available, or follow `references/INSTALL.md` manually. The script uses `apt` and therefore may require root privileges and network access for Ubuntu host-library dependencies.

## Run

After installation, use Darling normally, e.g. `darling shell <command>` or enter `darling shell`. For a user-supplied Mach-O compiler, first inspect it with `file` and, where available, `otool -L`/Mach-O inspection tools, then copy/mount it into a path visible inside Darling and execute it.

## Integrity and licensing

Before redistributing or modifying the bundled binaries, consult `../../../licenses/`, `../../../MANIFEST.sha256`, and `references/SOURCE-COMPLIANCE.md`. Do not remove license/copyright notices. The bundled Darling packages are unmodified release binaries.

## Deliberately omitted

Ruby and JavaScriptCore binary packages are omitted to keep the package below 100 MB. The tiny `darling` and `darling-extra` meta packages are also omitted because they depend on omitted packages. See `references/PACKAGES.md`.

## Limitation of a skill-only plugin

A skill does not itself provide an MCP process or hosted execution environment. The bundled binaries are supporting files for a compatible local/runner environment; whether ChatGPT can execute them depends on the host surface and its filesystem/process permissions.
