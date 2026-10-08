#!/usr/bin/env python3
"""Official Browser PKCE login with a user-local callback and remote exchange."""
import argparse
import base64
import hashlib
import hmac
import json
import os
from pathlib import Path
import re
import secrets
import tempfile
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import error, parse, request
import webbrowser

PUBLIC_REQUEST = None
CONNECT = "https://browser.lexmount.cn"
API = "https://api.lexmount.cn"
SCOPES = "browser:sessions browser:contexts browser:actions"


class AuthError(ValueError):
    """Only fixed, non-secret diagnostic messages may use this exception."""
    def __init__(self, code, message):
        super().__init__(message)
        self.code = code


def status(state_dir):
    state_dir = Path(state_dir)
    if (state_dir / "credentials.json").is_file():
        return {"status": "credentials_saved", "next": "Run official CLI doctor; saved credentials alone do not prove access"}
    if not (state_dir / "pending.json").is_file():
        return {"status": "request_missing", "next": "Create a new authorization helper in this task"}
    pending = load_json(state_dir / "pending.json")
    remaining = max(0, int(pending["expires_at"] - time.time()))
    return {"status": "waiting_for_authorization" if remaining else "request_expired",
            "expires_in_seconds": remaining,
            "next": "Complete login and return the result file" if remaining else "Create a new authorization helper; the old one cannot be resumed"}


def private_json(path, value):
    path = Path(path)
    fd, temporary = tempfile.mkstemp(dir=path.parent)
    try:
        with os.fdopen(fd, "w") as stream:
            json.dump(value, stream)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def load_json(path):
    path = Path(path)
    if path.stat().st_size > 32768:
        raise ValueError("Authorization file is too large")
    value = json.loads(path.read_text())
    if not isinstance(value, dict):
        raise ValueError("Invalid authorization file")
    return value


def begin(output_dir, private_root, client_name):
    if private_root is None:
        raise AuthError("private_storage_required", "Provide a private directory in the current task workspace")
    private_root = Path(private_root)
    output_dir = Path(output_dir).resolve()
    private_root = private_root.resolve()
    if private_root == output_dir or output_dir in private_root.parents:
        raise AuthError("unsafe_private_storage", "Private OAuth state must be outside the deliverable directory")
    private_root.mkdir(parents=True, exist_ok=True, mode=0o700)
    state_dir = Path(tempfile.mkdtemp(prefix="request-", dir=private_root))
    verifier = secrets.token_urlsafe(32)
    public = {"state": secrets.token_urlsafe(24),
              "challenge": base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest()).decode().rstrip("="),
              "expires_at": int(time.time()) + 1800,
              "client_name": client_name[:80]}
    private_json(state_dir / "pending.json", dict(public, verifier=verifier))
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    helper = output_dir / ("lexmount-authorize-" + public["state"][:8] + ".py")
    source = Path(__file__).read_text()
    source = source.replace("PUBLIC_REQUEST = None", "PUBLIC_REQUEST = " + repr(public), 1)
    with helper.open("x") as stream:
        stream.write(source)
    return {"status": "authorization_required", "helper_file": str(helper.resolve()),
            "state_dir": str(state_dir.resolve()),
            "credentials_file": str((state_dir / "credentials.json").resolve()),
            "expires_in_seconds": 1800}


def valid_redirect(value):
    u = parse.urlsplit(value)
    return (u.scheme == "http" and u.hostname == "127.0.0.1" and
            u.port is not None and 0 < u.port < 65536 and u.path == "/callback" and
            not u.username and not u.password and not u.query and not u.fragment)


def callback_handler(public, redirect_uri, result_path):
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *_):
            pass

        def do_GET(self):
            u = parse.urlsplit(self.path)
            q = parse.parse_qs(u.query, keep_blank_values=True)
            valid = (time.time() < public["expires_at"] and u.path == "/callback" and
                     self.headers.get("Host") == parse.urlsplit(redirect_uri).netloc and
                     len(q.get("state", [])) == 1 and
                     hmac.compare_digest(q["state"][0], public["state"]) and
                     len(q.get("code", [])) == 1 and
                     re.fullmatch(r"[A-Za-z0-9_-]{43}", q["code"][0]))
            if not valid:
                self.send_error(400, "Invalid or expired authorization callback")
                return
            private_json(result_path, {"state": public["state"], "code": q["code"][0],
                                       "redirect_uri": redirect_uri})
            self.server.complete = True
            body = ("<!doctype html><meta charset=utf-8><title>Lexmount authorization</title>"
                    "<h1>Authorization received</h1><p>Return to the same cloud task and attach the "
                    "lexmount-authorization-result JSON file saved next to the helper. "
                    "Do not paste its contents into chat.</p>").encode()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
    return Handler


def local_login(no_open=False):
    public = PUBLIC_REQUEST
    if not public or time.time() >= public["expires_at"]:
        raise AuthError("request_expired", "Authorization request expired; ask the same cloud task for a new helper")
    server = HTTPServer(("127.0.0.1", 0), BaseHTTPRequestHandler)
    redirect_uri = "http://127.0.0.1:%s/callback" % server.server_port
    result_path = Path(__file__).resolve().with_name(
        "lexmount-authorization-result-" + public["state"][:8] + ".json")
    server.RequestHandlerClass = callback_handler(public, redirect_uri, result_path)
    server.complete = False
    server.timeout = 1
    url = CONNECT + "/connect/codex?" + parse.urlencode({
        "source": "browser-cli", "intent": "agent-browser-control", "response": "code",
        "expires_in": "7d", "scope": SCOPES, "redirect_uri": redirect_uri,
        "state": public["state"], "code_challenge": public["challenge"],
        "code_challenge_method": "S256", "client_name": public["client_name"]})
    print(json.dumps({"status": "waiting_for_user_authorization", "authorization_url": url}), flush=True)
    try:
        if not no_open:
            webbrowser.open(url)
        while not server.complete and time.time() < public["expires_at"]:
            server.handle_request()
        if not server.complete:
            raise AuthError("callback_timeout", "No valid callback received before expiry; request a new helper")
        return {"status": "callback_received", "result_file": str(result_path),
                "next": "Attach this JSON file to the same cloud task within 10 minutes; do not paste its contents."}
    finally:
        server.server_close()


class NoRedirect(request.HTTPRedirectHandler):
    def redirect_request(self, *_):
        return None


def exchange(payload):
    req = request.Request(CONNECT + "/api/connect/codex/exchange",
                          data=json.dumps(payload).encode(),
                          headers={"Content-Type": "application/json", "Accept": "application/json"})
    try:
        with request.build_opener(NoRedirect).open(req, timeout=20) as response:
            raw = response.read(32769)
            if len(raw) > 32768:
                raise ValueError("Authorization response is too large")
            return json.loads(raw)
    except error.HTTPError as exc:
        raise AuthError("exchange_http_%s" % exc.code, "Official authorization exchange rejected (HTTP %s)" % exc.code) from None
    except (error.URLError, TimeoutError):
        raise AuthError("exchange_unreachable", "Official authorization exchange unavailable; check connectivity") from None


def extract_credentials(payload):
    if not isinstance(payload, dict):
        raise ValueError("Invalid authorization exchange response")
    candidates = [payload] + [payload[k] for k in ("credential", "credentials", "token", "env")
                              if isinstance(payload.get(k), dict)]
    for value in candidates:
        project = value.get("project_id") or value.get("projectId") or value.get("LEXMOUNT_PROJECT_ID") or payload.get("project_id")
        key = value.get("api_key") or value.get("apiKey") or value.get("LEXMOUNT_API_KEY") or payload.get("api_key")
        if not isinstance(project, str) or not project or not isinstance(key, str) or not key:
            continue
        api = value.get("api_base_url") or value.get("apiBaseUrl") or payload.get("api_base_url") or API
        if not isinstance(api, str) or api.rstrip("/") != API:
            raise AuthError("unexpected_api_endpoint", "Authorization returned an unexpected API endpoint")
        scopes = value.get("scopes") or value.get("scope") or payload.get("scopes") or SCOPES.split()
        if isinstance(scopes, str):
            scopes = scopes.split()
        return {"kind": "api_key", "project_id": project, "api_key": key,
                "api_base_url": API, "scopes": scopes,
                "source": "connect_from_browser_cli", "connect_base_url": CONNECT}
    raise ValueError("Official authorization response did not contain usable credentials")


def finish(state_dir, callback_file, exchange_fn=exchange):
    state_dir = Path(state_dir)
    if not (state_dir / "pending.json").is_file():
        raise AuthError("request_consumed" if (state_dir / "credentials.json").is_file() else "request_missing",
                        "No pending request remains in this task; check status before starting another login")
    if not Path(callback_file).is_file():
        raise AuthError("callback_file_missing", "The authorization result attachment is not present at the supplied path")
    lock = state_dir / "exchange.lock"
    fd = os.open(lock, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    os.close(fd)
    try:
        pending = load_json(state_dir / "pending.json")
        result = load_json(callback_file)
        if time.time() >= pending["expires_at"]:
            raise AuthError("request_expired", "Authorization request expired; generate a new helper")
        if not isinstance(result.get("state"), str) or not hmac.compare_digest(result["state"], pending["state"]):
            raise AuthError("state_mismatch", "Authorization result does not belong to this task")
        if not isinstance(result.get("code"), str) or not re.fullmatch(r"[A-Za-z0-9_-]{43}", result["code"]):
            raise AuthError("invalid_code", "Authorization result has an invalid code format")
        if not isinstance(result.get("redirect_uri"), str) or not valid_redirect(result["redirect_uri"]):
            raise AuthError("invalid_callback", "Authorization result has an invalid callback address")
        credentials = extract_credentials(exchange_fn({"code": result["code"],
            "code_verifier": pending["verifier"], "redirect_uri": result["redirect_uri"]}))
        path = state_dir / "credentials.json"
        private_json(path, credentials)
        (state_dir / "pending.json").unlink()
        return {"status": "authenticated", "credentials_file": str(path.resolve()),
                "api_key_redacted": True, "next": "Run official browser-cli doctor using this credentials file"}
    finally:
        lock.unlink()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", nargs="?", choices=["begin", "local", "finish", "status"],
                        default="local" if PUBLIC_REQUEST else None)
    parser.add_argument("--output-dir")
    parser.add_argument("--private-root", help="Private state directory in this task, outside the deliverable directory")
    parser.add_argument("--client-name", default="ChatGPT Work")
    parser.add_argument("--state-dir")
    parser.add_argument("--callback-file")
    parser.add_argument("--no-open", action="store_true")
    args = parser.parse_args()
    try:
        if args.operation == "begin" and args.output_dir:
            value = begin(args.output_dir, args.private_root, args.client_name)
        elif args.operation == "local":
            value = local_login(args.no_open)
        elif args.operation == "finish" and args.state_dir and args.callback_file:
            value = finish(args.state_dir, args.callback_file)
        elif args.operation == "status" and args.state_dir:
            value = status(args.state_dir)
        else:
            parser.error("begin requires --output-dir; finish requires --state-dir and --callback-file")
        print(json.dumps(value, ensure_ascii=False))
    except AuthError as exc:
        print(json.dumps({"status": "authorization_failed", "error": exc.code, "message": str(exc)}))
        raise SystemExit(1)
    except (ValueError, OSError, KeyError, TypeError):
        # File names and provider bodies can contain tokens; keep failures generic.
        print(json.dumps({"status": "authorization_failed", "error": "invalid_data_or_io_error", "message":
              "Authorization failed or expired. Verify the result belongs to this task; request a new helper if needed. No credentials were exposed."}))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
