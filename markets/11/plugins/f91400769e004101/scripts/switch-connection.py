#!/usr/bin/env python3
"""Launch real Codex OAuth and verify identity on one ephemeral runtime thread.

Uses Codex's credential store through supported APIs; never reads tokens.
The calling chat must independently re-read its identity and refresh tools.
"""
import argparse
import json
from pathlib import Path
import queue
import shutil
import subprocess
import sys
import threading
import time


def emit(event, **data):
    print(json.dumps({"event": event, **data}), flush=True)


class Runtime:
    def __init__(self, executable):
        self.process = subprocess.Popen(
            [executable, "app-server", "--stdio"], stdin=subprocess.PIPE,
            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True,
        )
        self.messages = queue.Queue()
        self.pending = []
        self.sequence = 0
        threading.Thread(target=self.read, daemon=True).start()

    def read(self):
        for line in self.process.stdout:
            try:
                self.messages.put(json.loads(line))
            except ValueError:
                pass
        self.messages.put({"closed": True})

    def send(self, message):
        self.process.stdin.write(json.dumps(message) + "\n")
        self.process.stdin.flush()

    def call(self, method, params, timeout=90):
        self.sequence += 1
        rid = self.sequence
        self.send({"jsonrpc": "2.0", "id": rid, "method": method, "params": params})
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            message = self.messages.get(timeout=max(.1, deadline-time.monotonic()))
            if message.get("closed"):
                raise RuntimeError("Codex runtime exited")
            if message.get("id") == rid:
                if "error" in message:
                    raise RuntimeError("Codex rejected " + method)
                return message.get("result")
            self.pending.append(message)
        raise RuntimeError("Codex request timed out")

    def wait_login(self, login_id, timeout):
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            message = self.pending.pop(0) if self.pending else self.messages.get(
                timeout=max(.1, deadline-time.monotonic()))
            if message.get("closed"):
                raise RuntimeError("Codex runtime exited during OAuth")
            if message.get("method") == "mcpServer/oauthLogin/completed":
                result = message["params"]
                if result.get("loginId") == login_id:
                    return bool(result.get("success"))
        return False

    def close(self):
        self.process.terminate()
        try:
            self.process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            self.process.kill()


def identity(runtime, thread_id, server):
    status = runtime.call("mcpServerStatus/list", {
        "threadId": thread_id, "serverName": server, "detail": "toolsAndAuthOnly",
    })
    names = set()
    for entry in status.get("data", []):
        if entry.get("name") == server:
            tools = entry.get("tools", {})
            names.update(tools if isinstance(tools, dict) else (t["name"] for t in tools))
    tool = next((name for name in ("get_workspace_overview", "get_current_identity",
                                  "get_current_principal") if name in names), None)
    if tool is None:
        raise RuntimeError("No supported Ando identity read is available; refresh the connection")
    result = runtime.call("mcpServer/tool/call", {
        "threadId": thread_id, "server": server, "tool": tool, "arguments": {},
    })
    if result.get("isError"):
        raise RuntimeError("Live Ando identity read failed")
    data = result.get("structuredContent")
    if data is None:
        data = json.loads(next(x["text"] for x in result["content"] if x["type"] == "text"))
    data = data.get("data", data)
    if tool == "get_workspace_overview":
        return {key: data[key] for key in ("principal", "workspace", "catalog_version")}
    source = data.get("principal", data.get("identity", {}))
    return {
        "principal": {"principal_type": source.get("principal_type", source.get("identity_type")),
                      "workspace_membership_id": source["workspace_membership_id"],
                      "display_name": source.get("display_name")},
        "workspace": {"id": source["workspace_id"], "name": source.get("workspace_name"),
                      "slug": source.get("workspace_slug")},
        "catalog_version": "legacy",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--server", required=True, help="Exact configured Codex MCP server name")
    parser.add_argument("--codex", help="Path to the host's Codex executable")
    parser.add_argument("--timeout", type=int, default=900)
    args = parser.parse_args()
    bundled = Path("/Applications/ChatGPT.app/Contents/Resources/codex-cli/CodexCLI.app/Contents/MacOS/codex")
    executable = args.codex or shutil.which("codex") or (str(bundled) if bundled.exists() else None)
    if not executable:
        parser.error("Codex is unavailable; use the plugin connection's OAuth control")
    config = json.loads(subprocess.check_output(
        [executable, "mcp", "get", args.server, "--json"], text=True, stderr=subprocess.DEVNULL))
    transport = config.get("transport", {})
    if (transport.get("url") != "https://mcp.ando.so/mcp"
            or transport.get("http_headers") or transport.get("env_http_headers")
            or transport.get("bearer_token_env_var")):
        parser.error("Requires the public Ando OAuth connection without credential/header overrides")
    runtime = Runtime(executable)
    try:
        runtime.call("initialize", {"clientInfo": {"name": "ando_connection_switch", "version": "1"},
                                    "capabilities": {"experimentalApi": True}})
        runtime.send({"jsonrpc": "2.0", "method": "initialized", "params": {}})
        thread = runtime.call("thread/start", {"ephemeral": True, "approvalPolicy": "never", "sandbox": "read-only"})
        tid = thread["thread"]["id"]
        emit("before", **identity(runtime, tid, args.server))
        login = runtime.call("mcpServer/oauth/login", {"name": args.server, "threadId": tid,
                                                       "timeoutSecs": args.timeout})
        emit("authorize", url=login["authorizationUrl"])
        if not runtime.wait_login(login["loginId"], args.timeout):
            raise RuntimeError("OAuth did not complete successfully; do not assume a switch")
        emit("after", verification_scope="diagnostic_runtime", **identity(runtime, tid, args.server))
        status = runtime.call("mcpServerStatus/list", {"threadId": tid, "serverName": args.server,
                                                       "detail": "toolsAndAuthOnly"})
        # Report names only, never credential/configuration payloads.
        servers = status.get("data", [])
        for server in servers:
            if server.get("name") == args.server:
                tools = server.get("tools", {})
                emit("runtime_tools", names=sorted(tools) if isinstance(tools, dict) else
                     sorted(t["name"] for t in tools))
        emit("verify_chat", status="pending_host_refresh", chat_switch_verified=False,
             instruction="OAuth completed in a separate diagnostic runtime. Refresh the actual calling chat's connection, then re-read its identity and inspect its callable tools. If refresh is unavailable mid-turn, continue verification on the next turn of the SAME chat. Do not report the switch complete or resume writes while verification is pending. If Codex stays stale or unauthenticated, fully quit and reopen the app, return to the SAME chat, and verify identity and tools again. Exit code 0 means helper success only.")
    finally:
        runtime.close()


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, subprocess.SubprocessError, queue.Empty, ValueError, KeyError) as error:
        emit("failed", reason=str(error) if isinstance(error, RuntimeError) else type(error).__name__)
        sys.exit(1)
