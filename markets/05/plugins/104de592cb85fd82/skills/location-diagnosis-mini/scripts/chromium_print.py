"""Measure and print one HTML in an isolated installed Chromium, using only stdlib.

DevTools is bound to loopback on an ephemeral port in a new temporary profile.
No user browser session, HTTP content server, package or alternate renderer is used.
"""

from __future__ import annotations

import base64
import hashlib
import json
import os
import signal
import socket
import struct
import subprocess
import tempfile
import time
from pathlib import Path
from typing import Any


class ChromiumError(Exception):
    pass


class LayoutOverflow(ChromiumError):
    def __init__(self, result: dict[str, Any]):
        super().__init__("印刷本文が紙面からはみ出しています。該当pageのreport JSONを修正してください")
        self.result = result


def stop_process(proc: subprocess.Popen[Any]) -> None:
    """Stop only the process group started with our own fresh profile."""
    if proc.poll() is not None:
        return
    try:
        if os.name == "posix":
            os.killpg(proc.pid, signal.SIGTERM)
        else:
            proc.terminate()
        proc.wait(timeout=5)
    except (ProcessLookupError, subprocess.TimeoutExpired):
        if proc.poll() is None:
            if os.name == "posix":
                os.killpg(proc.pid, signal.SIGKILL)
            else:
                proc.kill()
            proc.wait(timeout=5)


class DevTools:
    """Small serial JSON-over-WebSocket client for the local browser endpoint."""

    MAX_MESSAGE_BYTES = 128 * 1024 * 1024

    def __init__(self, port: int, endpoint: str, deadline: float):
        if not 1 <= port <= 65535 or not endpoint.startswith("/devtools/browser/"):
            raise ChromiumError("Chromeのlocal検査endpointが不正です")
        if any(char.isspace() for char in endpoint):
            raise ChromiumError("Chromeのlocal検査endpointが不正です")
        self.deadline = deadline
        self.buffer = b""
        self.sequence = 0
        self.sock = socket.create_connection(("127.0.0.1", port), self.remaining())
        try:
            key = base64.b64encode(os.urandom(16)).decode("ascii")
            request = (
                f"GET {endpoint} HTTP/1.1\r\nHost: 127.0.0.1:{port}\r\n"
                "Upgrade: websocket\r\nConnection: Upgrade\r\n"
                f"Sec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\n\r\n"
            )
            self.sock.sendall(request.encode("ascii"))
            response = b""
            while b"\r\n\r\n" not in response:
                self.sock.settimeout(self.remaining())
                chunk = self.sock.recv(4096)
                if not chunk or len(response) + len(chunk) > 16_384:
                    raise ChromiumError("Chromeのlocal接続を確立できません")
                response += chunk
            header, self.buffer = response.split(b"\r\n\r\n", 1)
            lines = header.decode("ascii").split("\r\n")
            fields = {name.lower(): value for line in lines[1:] if ":" in line
                      for name, value in [line.split(":", 1)]}
            expected = base64.b64encode(
                hashlib.sha1((key + "258EAFA5-E914-47DA-95CA-C5AB0DC85B11").encode()).digest()
            ).decode()
            if " 101 " not in lines[0] or fields.get("sec-websocket-accept", "").strip() != expected:
                raise ChromiumError("Chromeのlocal接続を検証できません")
        except BaseException:
            self.sock.close()
            raise

    def remaining(self) -> float:
        remaining = self.deadline - time.monotonic()
        if remaining <= 0:
            raise ChromiumError("Chromeの印刷検査・PDF生成がtimeoutしました")
        return remaining

    def read(self, count: int) -> bytes:
        while len(self.buffer) < count:
            self.sock.settimeout(self.remaining())
            chunk = self.sock.recv(min(65536, count - len(self.buffer)))
            if not chunk:
                raise ChromiumError("Chromeのlocal接続が途中で終了しました")
            self.buffer += chunk
        result, self.buffer = self.buffer[:count], self.buffer[count:]
        return result

    def send_frame(self, payload: bytes, opcode: int = 1) -> None:
        mask = os.urandom(4)
        length = len(payload)
        if length < 126:
            header = bytes((0x80 | opcode, 0x80 | length))
        elif length < 65536:
            header = bytes((0x80 | opcode, 0xFE)) + struct.pack("!H", length)
        else:
            header = bytes((0x80 | opcode, 0xFF)) + struct.pack("!Q", length)
        masked = bytes(value ^ mask[index % 4] for index, value in enumerate(payload))
        self.sock.settimeout(self.remaining())
        self.sock.sendall(header + mask + masked)

    def receive(self) -> dict[str, Any]:
        message = bytearray()
        while True:
            first, second = self.read(2)
            opcode = first & 0x0F
            length = second & 0x7F
            if length == 126:
                length = struct.unpack("!H", self.read(2))[0]
            elif length == 127:
                length = struct.unpack("!Q", self.read(8))[0]
            if second & 0x80 or first & 0x70 or len(message) + length > self.MAX_MESSAGE_BYTES:
                raise ChromiumError("Chromeのlocal応答frameが不正です")
            payload = self.read(length)
            if opcode == 8:
                raise ChromiumError("Chromeのlocal接続が終了しました")
            if opcode == 9:
                self.send_frame(payload, opcode=10)
                continue
            if opcode == 10:
                continue
            if opcode not in (0, 1):
                raise ChromiumError("Chromeのlocal応答形式が不正です")
            message.extend(payload)
            if first & 0x80:
                result = json.loads(message)
                if not isinstance(result, dict):
                    raise ChromiumError("Chromeのlocal応答がJSON objectではありません")
                return result

    def call(self, method: str, params: dict[str, Any] | None = None,
             session: str | None = None) -> dict[str, Any]:
        self.sequence += 1
        request: dict[str, Any] = {"id": self.sequence, "method": method, "params": params or {}}
        if session:
            request["sessionId"] = session
        self.send_frame(json.dumps(request).encode("utf-8"))
        while True:
            response = self.receive()
            if response.get("id") != self.sequence:
                continue  # Asynchronous page events are not command receipts.
            if "error" in response:
                raise ChromiumError(f"Chrome {method}: {response['error'].get('message', '失敗')}")
            return response.get("result", {})

    def evaluate(self, expression: str, session: str) -> Any:
        response = self.call("Runtime.evaluate", {
            "expression": expression, "returnByValue": True, "awaitPromise": True,
        }, session)
        if "exceptionDetails" in response:
            raise ChromiumError("Chromeの印刷レイアウト検査を実行できません")
        return response.get("result", {}).get("value")

    def close(self) -> None:
        self.sock.close()


def measure_and_print(browser: Path, html_path: Path, output_path: Path,
                      timeout: int) -> dict[str, Any]:
    """The same page, print media and loaded fonts are used for measure + PDF."""
    deadline = time.monotonic() + timeout
    with tempfile.TemporaryDirectory(prefix="rognalia-headless-profile-") as profile_dir:
        command = [str(browser), "--headless=new", "--disable-gpu",
                   "--disable-background-networking", "--disable-component-update",
                   "--disable-default-apps", "--disable-extensions", "--disable-sync",
                   "--metrics-recording-only", "--no-default-browser-check", "--no-first-run",
                   "--remote-debugging-address=127.0.0.1", "--remote-debugging-port=0",
                   f"--user-data-dir={profile_dir}", "about:blank"]
        with tempfile.TemporaryFile() as log:
            proc = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT,
                                    start_new_session=True)
            client = None
            try:
                active_port = Path(profile_dir) / "DevToolsActivePort"
                while not active_port.is_file():
                    if proc.poll() is not None:
                        raise ChromiumError("Chromeを起動できませんでした")
                    if time.monotonic() >= deadline:
                        raise ChromiumError("Chromeの起動がtimeoutしました")
                    time.sleep(0.05)
                # Read only our new profile's endpoint, never discover another browser.
                endpoint = active_port.read_text(encoding="utf-8").splitlines()
                client = DevTools(int(endpoint[0]), endpoint[1], deadline)
                target = client.call("Target.createTarget", {"url": "about:blank"})["targetId"]
                session = client.call("Target.attachToTarget", {
                    "targetId": target, "flatten": True,
                })["sessionId"]
                client.call("Page.enable", session=session)
                client.call("Emulation.setDeviceMetricsOverride", {
                    "width": 794, "height": 1123, "deviceScaleFactor": 1, "mobile": False,
                }, session)
                client.call("Emulation.setEmulatedMedia", {"media": "print"}, session)
                navigation = client.call("Page.navigate", {"url": html_path.as_uri()}, session)
                if navigation.get("errorText"):
                    raise ChromiumError("Chromeが入力HTMLを開けませんでした")
                expected_url = json.dumps(html_path.as_uri())
                while not client.evaluate(
                    f"document.URL === {expected_url} && document.readyState === 'complete'", session
                ):
                    client.remaining()
                    time.sleep(0.05)
                client.evaluate("(async () => { await document.fonts.ready; "
                                "await new Promise(r => requestAnimationFrame(r)); return true; })()",
                                session)
                script = Path(__file__).with_name("print_layout.js").read_text(encoding="utf-8")
                layout = client.evaluate(script, session)
                if not isinstance(layout, dict) or layout.get("status") not in ("ok", "overflow"):
                    raise ChromiumError("Chromeの印刷レイアウト検査結果が不正です")
                if layout["status"] == "overflow":
                    raise LayoutOverflow(layout)
                pdf = client.call("Page.printToPDF", {
                    "printBackground": True, "displayHeaderFooter": False,
                    "preferCSSPageSize": True, "paperWidth": 210 / 25.4,
                    "paperHeight": 297 / 25.4, "marginTop": 0, "marginBottom": 0,
                    "marginLeft": 0, "marginRight": 0,
                }, session)
                payload = base64.b64decode(pdf["data"], validate=True)
                output_path.write_bytes(payload)
                return layout
            finally:
                if client:
                    client.close()
                stop_process(proc)
