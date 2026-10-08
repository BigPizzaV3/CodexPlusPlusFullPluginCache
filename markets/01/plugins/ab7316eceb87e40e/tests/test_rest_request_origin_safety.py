"""Origin-safety regression coverage for the generic REST clients."""

from __future__ import annotations

import importlib.util
import json
import re
import unittest
from pathlib import Path
from typing import Any
from unittest.mock import Mock, patch
from urllib.parse import urlsplit

PLUGIN_ROOT = Path(__file__).resolve().parents[1]
CLIENT_PATHS = sorted(PLUGIN_ROOT.glob("skills/*/scripts/rest_request.py"))
EQTLCAT_CLIENT = PLUGIN_ROOT / "skills" / "eqtl-catalogue-skill" / "scripts" / "rest_request.py"
REGISTRY = json.loads(
    (PLUGIN_ROOT / "references" / "source-links.json").read_text(encoding="utf-8")
)["skills"]


def _load_module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _registered_base_url(skill_name: str) -> str:
    return str(REGISTRY[skill_name]["request_url_prefixes"][0]).rstrip("/")


def _documented_rest_payloads() -> list[tuple[str, dict[str, Any]]]:
    """Extract the JSON payloads in each REST skill's Common patterns section."""
    payloads: list[tuple[str, dict[str, Any]]] = []
    for client_path in CLIENT_PATHS:
        skill_name = client_path.parents[1].name
        document = (client_path.parents[1] / "SKILL.md").read_text(encoding="utf-8")
        heading = re.search(r"^- Common .* patterns:\s*$", document, flags=re.MULTILINE)
        if heading is None:
            raise AssertionError(f"{skill_name} does not document common REST payloads")
        section_end = document.find("\n## Output", heading.end())
        if section_end < 0:
            raise AssertionError(f"{skill_name} common REST payload section has no end")
        for line in document[heading.end() : section_end].splitlines():
            match = re.search(r"\{.*\}", line)
            if match is None:
                continue
            payload = json.loads(match.group(0))
            if isinstance(payload, dict) and "base_url" in payload:
                payloads.append((skill_name, payload))
    return payloads


class RestRequestOriginSafetyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.clients = [
            (path.parents[1].name, _load_module(f"origin_safety_client_{index}", path))
            for index, path in enumerate(CLIENT_PATHS)
        ]

    def test_generic_clients_delegate_to_one_shared_implementation(self) -> None:
        expected_rest_skills = {
            skill_name
            for skill_name, entry in REGISTRY.items()
            if entry.get("request_url_prefixes")
        }
        self.assertEqual(expected_rest_skills, {path.parents[1].name for path in CLIENT_PATHS})
        generic_clients = [path for path in CLIENT_PATHS if path != EQTLCAT_CLIENT]
        shared_client = PLUGIN_ROOT / "scripts" / "database_rest_client.py"
        self.assertTrue(generic_clients)
        self.assertTrue(shared_client.is_file())
        for client in generic_clients:
            with self.subTest(skill=client.parents[1].name):
                self.assertIn("database_rest_client", client.read_text(encoding="utf-8"))
                self.assertLess(client.stat().st_size, shared_client.stat().st_size)
        self.assertNotIn("database_rest_client", EQTLCAT_CLIENT.read_text(encoding="utf-8"))

    def test_all_clients_preserve_relative_paths(self) -> None:
        for skill_name, client in self.clients:
            base_url = _registered_base_url(skill_name)
            with self.subTest(skill=skill_name):
                self.assertEqual(
                    f"{base_url}/records?gene=TP53",
                    client._build_url(base_url, "records?gene=TP53"),
                )

    def test_all_clients_accept_same_origin_absolute_urls_with_normalization(
        self,
    ) -> None:
        for skill_name, client in self.clients:
            registered = urlsplit(_registered_base_url(skill_name))
            hostname = registered.hostname
            self.assertIsNotNone(hostname)
            prefix_path = registered.path.rstrip("/")
            base_url = f"https://{hostname.upper()}{prefix_path}"
            absolute_path = f"HTTPS://{hostname}{prefix_path}/records"
            with self.subTest(skill=skill_name):
                self.assertEqual(
                    absolute_path,
                    client._build_url(base_url, absolute_path),
                )

    def test_all_clients_reject_noncanonical_origin_spellings_before_session(
        self,
    ) -> None:
        for skill_name, client in self.clients:
            registered_url = _registered_base_url(skill_name)
            registered = urlsplit(registered_url)
            hostname = registered.hostname
            self.assertIsNotNone(hostname)
            prefix_path = registered.path.rstrip("/")
            payloads = (
                {
                    "base_url": f"https://{hostname}:443{prefix_path}",
                    "path": "records",
                },
                {
                    "base_url": f"https://{hostname}:{prefix_path}",
                    "path": "records",
                },
                {
                    "base_url": f"https://{hostname}:not-a-port{prefix_path}",
                    "path": "records",
                },
                {
                    "base_url": f"https://{hostname}.{prefix_path}",
                    "path": "records",
                },
                {
                    "base_url": registered_url,
                    "path": f"https://{hostname}:443{prefix_path}/records",
                },
                {
                    "base_url": registered_url,
                    "path": f"https://{hostname}:{prefix_path}/records",
                },
                {
                    "base_url": registered_url,
                    "path": f"https://{hostname}:not-a-port{prefix_path}/records",
                },
                {
                    "base_url": registered_url,
                    "path": f"https://{hostname}.{prefix_path}/records",
                },
            )
            for payload in payloads:
                session_factory = Mock()
                with self.subTest(skill=skill_name, payload=payload):
                    with patch.object(client.requests, "Session", session_factory):
                        output = client.execute(payload)

                    self.assertFalse(output["ok"])
                    self.assertEqual("invalid_input", output["error"]["code"])
                    self.assertNotIn("sources", output)
                    self.assertNotIn("checked_sources", output)
                    session_factory.assert_not_called()
                    session_factory.return_value.request.assert_not_called()

    def test_clients_reject_other_sources_on_shared_registered_hosts(self) -> None:
        client = next(client for skill_name, client in self.clients if skill_name == "chembl-skill")
        base_url = "https://www.ebi.ac.uk/chembl/api/data"
        for path in (
            "https://alphafold.ebi.ac.uk/api/prediction/P04637",
            "https://www.ebi.ac.uk/chebi/backend/api/public/compound/CHEBI:15377",
            "../../chebi/backend/api/public/compound/CHEBI:15377",
            "%2525252e%2525252e/chebi/backend/api/public",
            "%2e%2e%5cchebi/backend/api/public",
            "..%5cchebi/backend/api/public",
            "x/..;/chebi/backend/api/public",
            "x/%2e%2e%3b/chebi/backend/api/public",
        ):
            with self.subTest(path=path):
                with self.assertRaises(ValueError):
                    client._build_url(base_url, path)

    def test_all_clients_validate_base_scope_independently_before_session(self) -> None:
        for skill_name, client in self.clients:
            registered_prefix = str(REGISTRY[skill_name]["request_url_prefixes"][0])
            parsed = urlsplit(registered_prefix)
            self.assertIsNotNone(parsed.hostname)
            wrong_base = f"https://{parsed.hostname}/__unregistered_base_scope__"
            if client.is_registered_source_base_url(skill_name, wrong_base):
                wrong_base = "https://unregistered-source.example/__wrong_base_scope__"
            candidate = registered_prefix.rstrip("/") + "/records"
            self.assertTrue(client.is_registered_source_url(skill_name, candidate))
            self.assertFalse(client.is_registered_source_base_url(skill_name, wrong_base))

            session_factory = Mock()
            with self.subTest(skill=skill_name, base_url=wrong_base):
                with patch.object(client.requests, "Session", session_factory):
                    output = client.execute({"base_url": wrong_base, "path": candidate})

                self.assertFalse(output["ok"])
                self.assertEqual("invalid_input", output["error"]["code"])
                self.assertNotIn("sources", output)
                self.assertNotIn("checked_sources", output)
                session_factory.assert_not_called()
                session_factory.return_value.request.assert_not_called()

    def test_chembl_rejects_chebi_base_with_absolute_valid_candidate(self) -> None:
        skill_name = "chembl-skill"
        client = next(client for name, client in self.clients if name == skill_name)
        candidate = "https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL25.json"
        payload = {
            "base_url": "https://www.ebi.ac.uk/chebi/backend/api/public",
            "path": candidate,
        }
        self.assertTrue(client.is_registered_source_url(skill_name, candidate))
        self.assertFalse(client.is_registered_source_base_url(skill_name, payload["base_url"]))

        session_factory = Mock()
        with patch.object(client.requests, "Session", session_factory):
            output = client.execute(payload)

        self.assertFalse(output["ok"])
        self.assertEqual("invalid_input", output["error"]["code"])
        self.assertNotIn("sources", output)
        self.assertNotIn("checked_sources", output)
        session_factory.assert_not_called()
        session_factory.return_value.request.assert_not_called()

    def test_all_documented_rest_payloads_use_accepted_base_scopes(self) -> None:
        clients = dict(self.clients)
        payloads = _documented_rest_payloads()
        self.assertEqual(set(clients), {skill_name for skill_name, _ in payloads})
        for skill_name, payload in payloads:
            client = clients[skill_name]
            base_url = payload["base_url"]
            path = payload["path"]
            with self.subTest(skill=skill_name, base_url=base_url, path=path):
                self.assertTrue(client.is_registered_source_base_url(skill_name, base_url))
                candidate = client._build_url(base_url, path)
                self.assertTrue(client.is_registered_source_url(skill_name, candidate))

    def test_all_clients_omit_raw_query_values_from_success_outputs(self) -> None:
        raw_path = "records?api_key=TOPSECRET&query=private-patient&format=json"
        for skill_name, client in self.clients:
            base_url = _registered_base_url(skill_name)
            request_url = f"{base_url}/{raw_path}"
            for response_format in ("json", "text"):
                response = Mock()
                response.status_code = 200
                response.url = request_url
                response.history = []
                if response_format == "json":
                    body = {"results": [{"id": "record"}]}
                    response.headers = {"content-type": "application/json"}
                    response.text = json.dumps(body)
                    response.content = response.text.encode("utf-8")
                    response.json.return_value = body
                else:
                    response.headers = {"content-type": "text/plain"}
                    response.text = "returned biological source evidence"
                    response.content = response.text.encode("utf-8")
                session = Mock()
                session.request.return_value = response

                with self.subTest(skill=skill_name, response_format=response_format):
                    with patch.object(client.requests, "Session", return_value=session):
                        output = client.execute(
                            {
                                "base_url": base_url,
                                "path": raw_path,
                                "response_format": response_format,
                            }
                        )

                    self.assertTrue(output["ok"])
                    self.assertEqual("records", output["path"])
                    serialized = json.dumps(output)
                    self.assertNotIn("TOPSECRET", serialized)
                    self.assertNotIn("private-patient", serialized)
                    requested_method, requested_url = session.request.call_args.args[:2]
                    self.assertEqual("GET", requested_method)
                    self.assertEqual(request_url, requested_url)
                    session.close.assert_called_once_with()

    def test_sanitized_path_preserves_metadata_endpoint_classification(self) -> None:
        skill_name, client = self.clients[0]
        base_url = _registered_base_url(skill_name)
        response = Mock()
        response.status_code = 200
        response.url = f"{base_url}/ping?api_key=TOPSECRET&query=private-patient"
        response.history = []
        response.headers = {"content-type": "application/json"}
        response.text = '{"status": "ok"}'
        response.content = response.text.encode("utf-8")
        response.json.return_value = {"status": "ok"}
        session = Mock()
        session.request.return_value = response

        with patch.object(client.requests, "Session", return_value=session):
            output = client.execute(
                {
                    "base_url": base_url,
                    "path": "ping?api_key=TOPSECRET&query=private-patient",
                }
            )

        self.assertTrue(output["ok"])
        self.assertEqual("ping", output["path"])
        self.assertNotIn("sources", output)
        self.assertEqual("metadata", output["checked_sources"][0]["reason"])
        self.assertNotIn("TOPSECRET", json.dumps(output))
        self.assertNotIn("private-patient", json.dumps(output))
        session.close.assert_called_once_with()

    def test_all_clients_disable_redirects_before_sending_headers_or_bodies(self) -> None:
        for skill_name, client in self.clients:
            base_url = _registered_base_url(skill_name)
            request_url = f"{base_url}/submit?api_key=TOPSECRET"
            response = Mock()
            response.status_code = 307
            response.url = request_url
            response.history = []
            response.headers = {"location": "https://other.example.org/collect"}
            response.text = "redirect"
            response.content = b"redirect"
            session = Mock()
            session.request.return_value = response

            with self.subTest(skill=skill_name):
                with patch.object(client.requests, "Session", return_value=session):
                    output = client.execute(
                        {
                            "base_url": base_url,
                            "path": "submit?api_key=TOPSECRET",
                            "method": "POST",
                            "headers": {"X-API-Key": "HEADER-SECRET"},
                            "json_body": {"query": "BODY-SECRET"},
                        }
                    )

                self.assertFalse(output["ok"])
                self.assertEqual("invalid_response", output["error"]["code"])
                self.assertNotIn("sources", output)
                self.assertNotIn("checked_sources", output)
                serialized = json.dumps(output)
                self.assertNotIn("TOPSECRET", serialized)
                self.assertNotIn("HEADER-SECRET", serialized)
                self.assertNotIn("BODY-SECRET", serialized)
                session.request.assert_called_once_with(
                    "POST",
                    request_url,
                    params={},
                    timeout=30,
                    allow_redirects=False,
                    json={"query": "BODY-SECRET"},
                )
                response.raise_for_status.assert_not_called()
                session.close.assert_called_once_with()

    def test_all_clients_redact_value_errors_during_session_header_setup(self) -> None:
        for skill_name, client in self.clients:
            session = Mock()
            session.headers.update.side_effect = ValueError("HEADER-SECRET")

            with self.subTest(skill=skill_name):
                with patch.object(client.requests, "Session", return_value=session):
                    output = client.execute(
                        {
                            "base_url": _registered_base_url(skill_name),
                            "path": "records",
                        }
                    )

                self.assertFalse(output["ok"])
                self.assertEqual("invalid_response", output["error"]["code"])
                self.assertEqual(
                    f"Response validation failed for {skill_name}.",
                    output["error"]["message"],
                )
                self.assertNotIn("HEADER-SECRET", json.dumps(output))
                self.assertNotIn("sources", output)
                self.assertNotIn("checked_sources", output)
                session.request.assert_not_called()
                session.close.assert_called_once_with()

    def test_all_clients_sanitize_session_construction_failures_without_close(
        self,
    ) -> None:
        for skill_name, client in self.clients:
            cases = (
                (
                    ValueError("SESSION-VALUE-SECRET"),
                    "invalid_response",
                    f"Response validation failed for {skill_name}.",
                ),
                (
                    client.requests.RequestException("SESSION-REQUEST-SECRET"),
                    "network_error",
                    f"Request failed for {skill_name}: RequestException",
                ),
                (
                    RuntimeError("SESSION-RUNTIME-SECRET"),
                    "invalid_response",
                    f"Unexpected response processing failure for {skill_name}.",
                ),
            )
            for exception, error_code, message in cases:
                session_factory = Mock(side_effect=exception)

                with self.subTest(skill=skill_name, exception=type(exception).__name__):
                    with patch.object(client.requests, "Session", session_factory):
                        output = client.execute(
                            {
                                "base_url": _registered_base_url(skill_name),
                                "path": "records",
                            }
                        )

                    self.assertFalse(output["ok"])
                    self.assertEqual(error_code, output["error"]["code"])
                    self.assertEqual(message, output["error"]["message"])
                    serialized = json.dumps(output)
                    self.assertNotIn("SECRET", serialized)
                    self.assertNotIn("sources", output)
                    self.assertNotIn("checked_sources", output)
                    session_factory.assert_called_once_with()
                    session_factory.return_value.request.assert_not_called()
                    session_factory.return_value.close.assert_not_called()

    def test_all_clients_redact_value_errors_during_response_parsing(self) -> None:
        for skill_name, client in self.clients:
            base_url = _registered_base_url(skill_name)
            response = Mock()
            response.status_code = 200
            response.url = f"{base_url}/records"
            response.history = []
            response.headers = {"content-type": "application/json"}
            response.text = '{"results": [{"id": "record"}]}'
            response.content = response.text.encode("utf-8")
            response.json.side_effect = ValueError("parse failed near BODY-SECRET")
            session = Mock()
            session.request.return_value = response

            with self.subTest(skill=skill_name):
                with patch.object(client.requests, "Session", return_value=session):
                    output = client.execute(
                        {
                            "base_url": base_url,
                            "path": "records",
                            "response_format": "json",
                        }
                    )

                self.assertFalse(output["ok"])
                self.assertEqual("invalid_response", output["error"]["code"])
                self.assertEqual(
                    f"Response validation failed for {skill_name}.",
                    output["error"]["message"],
                )
                self.assertNotIn("BODY-SECRET", json.dumps(output))
                self.assertNotIn("sources", output)
                self.assertNotIn("checked_sources", output)
                response.raise_for_status.assert_called_once_with()
                session.close.assert_called_once_with()

    def test_all_clients_redact_unexpected_post_session_exceptions(self) -> None:
        for skill_name, client in self.clients:
            session = Mock()
            session.request.side_effect = RuntimeError("BODY-SECRET")

            with self.subTest(skill=skill_name):
                with patch.object(client.requests, "Session", return_value=session):
                    output = client.execute(
                        {
                            "base_url": _registered_base_url(skill_name),
                            "path": "records",
                        }
                    )

                self.assertFalse(output["ok"])
                self.assertEqual("invalid_response", output["error"]["code"])
                self.assertEqual(
                    f"Unexpected response processing failure for {skill_name}.",
                    output["error"]["message"],
                )
                self.assertNotIn("BODY-SECRET", json.dumps(output))
                self.assertNotIn("sources", output)
                self.assertNotIn("checked_sources", output)
                session.request.assert_called_once()
                session.close.assert_called_once_with()

    def test_all_clients_suppress_close_errors_without_overriding_sanitized_errors(
        self,
    ) -> None:
        for skill_name, client in self.clients:
            session = Mock()
            session.request.side_effect = RuntimeError("REQUEST-SECRET")
            session.close.side_effect = RuntimeError("CLOSE-SECRET")

            with self.subTest(skill=skill_name):
                with patch.object(client.requests, "Session", return_value=session):
                    output = client.execute(
                        {
                            "base_url": _registered_base_url(skill_name),
                            "path": "records",
                        }
                    )

                self.assertFalse(output["ok"])
                self.assertEqual("invalid_response", output["error"]["code"])
                self.assertEqual(
                    f"Unexpected response processing failure for {skill_name}.",
                    output["error"]["message"],
                )
                serialized = json.dumps(output)
                self.assertNotIn("REQUEST-SECRET", serialized)
                self.assertNotIn("CLOSE-SECRET", serialized)
                self.assertNotIn("sources", output)
                self.assertNotIn("checked_sources", output)
                session.request.assert_called_once()
                session.close.assert_called_once_with()

    def test_all_clients_reject_cross_origin_absolute_paths(self) -> None:
        for skill_name, client in self.clients:
            base_url = _registered_base_url(skill_name)
            hostname = urlsplit(base_url).hostname
            self.assertIsNotNone(hostname)
            absolute_paths = (
                "https://other.example.org/records",
                f"http://{hostname}/records",
                f"https://{hostname}:444/records",
                f"https://{hostname}:0/records",
            )
            for absolute_path in absolute_paths:
                with self.subTest(
                    skill=skill_name,
                    base_url=base_url,
                    absolute_path=absolute_path,
                ):
                    with self.assertRaisesRegex(ValueError, "must share"):
                        client._build_url(base_url, absolute_path)

    def test_all_clients_reject_malformed_or_credentialed_urls(self) -> None:
        for skill_name, client in self.clients:
            base_url = _registered_base_url(skill_name)
            hostname = urlsplit(base_url).hostname
            self.assertIsNotNone(hostname)
            bad_cases = (
                (f"https://user:secret@{hostname}", "records"),
                (base_url, f"https://user:secret@{hostname}/records"),
                (f"https://{hostname}:not-a-port", "records"),
                ("https://api..example.org", "records"),
                (base_url, f"ftp://{hostname}/records"),
                (base_url, f"//{hostname}/records"),
                (base_url, f"https://{hostname}\\@other.example/records"),
            )
            for base_url, path in bad_cases:
                with self.subTest(skill=skill_name, base_url=base_url, path=path):
                    with self.assertRaises(ValueError):
                        client._build_url(base_url, path)

    def test_invalid_request_origin_returns_sanitized_error_before_session_creation(
        self,
    ) -> None:
        for skill_name, client in self.clients:
            base_url = _registered_base_url(skill_name)
            hostname = urlsplit(base_url).hostname
            self.assertIsNotNone(hostname)
            cases = (
                ({"base_url": "https://example.org", "path": "records"}, "example.org"),
                (
                    {
                        "base_url": "https://ｗｗｗ．ｅｂｉ．ａｃ．ｕｋ/chembl/api/data",
                        "path": "records",
                    },
                    "unicode-host",
                ),
                (
                    {
                        "base_url": "https://www。ebi。ac。uk/chembl/api/data",
                        "path": "records",
                    },
                    "unicode-host",
                ),
                (
                    {
                        "base_url": "https://www.ｅbi.ac.uk/chembl/api/data",
                        "path": "records",
                    },
                    "unicode-host",
                ),
                (
                    {
                        "base_url": base_url,
                        "path": f"https://user:secret@{hostname}/records",
                    },
                    "secret",
                ),
            )
            for payload, forbidden in cases:
                session_factory = Mock()
                with self.subTest(skill=skill_name, payload=payload):
                    with patch.object(client.requests, "Session", session_factory):
                        output = client.execute(payload)

                    self.assertFalse(output["ok"])
                    self.assertEqual("invalid_input", output["error"]["code"])
                    self.assertNotIn("sources", output)
                    self.assertNotIn("checked_sources", output)
                    if forbidden != "unicode-host":
                        self.assertNotIn(forbidden, json.dumps(output))
                    session_factory.assert_not_called()

    def test_invalid_headers_and_boolean_limits_fail_before_session_creation(self) -> None:
        for skill_name, client in self.clients:
            invalid_fields = (
                {"headers": {1: "bad-key"}},
                {"headers": {"Bad Header": "TOPSECRET"}},
                {"headers": {"X-Test": "private\r\nX-Injected: TOPSECRET"}},
                {"headers": {"Host": "other.example.org"}},
                {"headers": {"X-Forwarded-Host": "other.example.org"}},
                {"headers": {"Content-Length": "1"}},
                {"headers": {"X-Test": "\x00TOPSECRET"}},
                {"headers": {"X-Test": "emoji-🔒"}},
                {"timeout_sec": True},
                {"max_items": True},
            )
            for invalid in invalid_fields:
                session_factory = Mock()
                with self.subTest(skill=skill_name, invalid=invalid):
                    with patch.object(client.requests, "Session", session_factory):
                        output = client.execute(
                            {
                                "base_url": _registered_base_url(skill_name),
                                "path": "records",
                                **invalid,
                            }
                        )

                    self.assertFalse(output["ok"])
                    self.assertEqual("invalid_input", output["error"]["code"])
                    self.assertNotIn("sources", output)
                    self.assertNotIn("checked_sources", output)
                    self.assertNotIn("TOPSECRET", json.dumps(output))
                    session_factory.assert_not_called()

    def test_all_clients_reject_routing_method_and_framing_override_headers(
        self,
    ) -> None:
        blocked_headers = (
            "Host",
            "Proxy",
            "Proxy-Connection",
            "Connection",
            "TE",
            "Trailer",
            "Transfer-Encoding",
            "Upgrade",
            "Content-Length",
            "Forwarded",
            "Via",
            "Max-Forwards",
            "Keep-Alive",
            "Proxy-Authenticate",
            "Proxy-Authorization",
            "X-Forwarded-For",
            "X-Forwarded-Host",
            "X-Forwarded-Port",
            "X-Forwarded-Prefix",
            "X-Forwarded-Proto",
            "X-Forwarded-Uri",
            "X-Real-IP",
            "X-HTTP-Method-Override",
            "X-Method-Override",
            "X-HTTP-Method",
            "X-Envoy-Original-Path",
            "X-Original-Host",
            "X-Original-URI",
            "X-Original-URL",
            "X-Rewrite-URL",
            "X-Host",
            "X-HTTP-Host-Override",
            "X-Forwarded",
            "X-Rewrite-Host",
            "X-Backend-Host",
            "hOsT",
            "PROXY_CONNECTION",
            "x_fOrWaRdEd_fOr",
            "X_HTTP_METHOD_OVERRIDE",
            "X_ORIGINAL_URI",
            "x_hOsT",
            "X_HTTP_HOST_OVERRIDE",
            "x_fOrWaRdEd",
            "X_REWRITE_HOST",
            "x_bAcKeNd_hOsT",
        )
        for skill_name, client in self.clients:
            for header_name in blocked_headers:
                session_factory = Mock()
                with self.subTest(skill=skill_name, header=header_name):
                    with patch.object(client.requests, "Session", session_factory):
                        output = client.execute(
                            {
                                "base_url": _registered_base_url(skill_name),
                                "path": "records",
                                "headers": {header_name: "ROUTING-HEADER-SECRET"},
                            }
                        )

                    self.assertFalse(output["ok"])
                    self.assertEqual("invalid_input", output["error"]["code"])
                    self.assertNotIn("sources", output)
                    self.assertNotIn("checked_sources", output)
                    self.assertNotIn("ROUTING-HEADER-SECRET", json.dumps(output))
                    session_factory.assert_not_called()
                    session_factory.return_value.request.assert_not_called()

    def test_all_clients_preserve_safe_accept_and_user_agent_headers(self) -> None:
        safe_headers = {
            "Accept": "application/json",
            "User-Agent": "life-sciences-client/1.0",
            "X-Request-ID": "public-request-id",
        }
        for skill_name, client in self.clients:
            with self.subTest(skill=skill_name):
                self.assertEqual(
                    safe_headers,
                    client._require_headers("headers", safe_headers),
                )

    def test_final_cross_origin_redirect_is_not_presented_as_evidence(self) -> None:
        for skill_name, client in self.clients:
            base_url = _registered_base_url(skill_name)
            response = Mock()
            response.status_code = 200
            response.headers = {"content-type": "application/json"}
            response.url = "https://other.example.org/records?api_key=secret&query=private-patient"
            response.history = []
            response.text = json.dumps({"results": [{"id": "record"}]})
            response.content = response.text.encode("utf-8")
            response.json.return_value = {"results": [{"id": "record"}]}
            session = Mock()
            session.request.return_value = response

            with self.subTest(skill=skill_name):
                with patch.object(client.requests, "Session", return_value=session):
                    output = client.execute({"base_url": base_url, "path": "records"})

                self.assertFalse(output["ok"])
                self.assertEqual("invalid_response", output["error"]["code"])
                self.assertNotIn("sources", output)
                self.assertNotIn("checked_sources", output)
                self.assertNotIn("secret", json.dumps(output))
                self.assertNotIn("private-patient", json.dumps(output))
                session.close.assert_called_once_with()

    def test_intermediate_cross_origin_redirect_is_rejected(self) -> None:
        skill_name, client = self.clients[0]
        base_url = _registered_base_url(skill_name)
        redirect = Mock()
        redirect.url = "https://other.example.org/intermediate"
        response = Mock()
        response.status_code = 200
        response.headers = {"content-type": "application/json"}
        response.url = f"{base_url}/final"
        response.history = [redirect]
        response.text = '{"results": [{"id": "record"}]}'
        response.content = response.text.encode("utf-8")
        response.json.return_value = {"results": [{"id": "record"}]}
        session = Mock()
        session.request.return_value = response

        with patch.object(client.requests, "Session", return_value=session):
            output = client.execute({"base_url": base_url, "path": "records"})

        self.assertFalse(output["ok"])
        self.assertEqual("invalid_response", output["error"]["code"])
        self.assertNotIn("sources", output)
        session.close.assert_called_once_with()

    def test_all_clients_reject_same_scope_redirect_history_when_disabled(self) -> None:
        for skill_name, client in self.clients:
            base_url = _registered_base_url(skill_name)
            redirect = Mock()
            redirect.status_code = 302
            redirect.url = f"{base_url}/redirect"
            response = Mock()
            response.status_code = 200
            response.headers = {"content-type": "application/json"}
            response.url = f"{base_url}/records"
            response.history = [redirect]
            response.text = '{"results": [{"id": "record"}]}'
            response.content = response.text.encode("utf-8")
            response.json.return_value = {"results": [{"id": "record"}]}
            session = Mock()
            session.request.return_value = response

            with self.subTest(skill=skill_name):
                with patch.object(client.requests, "Session", return_value=session):
                    output = client.execute({"base_url": base_url, "path": "records"})

                self.assertFalse(output["ok"])
                self.assertEqual("invalid_response", output["error"]["code"])
                self.assertNotIn("sources", output)
                self.assertNotIn("checked_sources", output)
                self.assertFalse(session.request.call_args.kwargs["allow_redirects"])
                response.raise_for_status.assert_not_called()
                session.close.assert_called_once_with()

    def test_same_origin_redirect_history_cannot_cross_registered_source_scopes(
        self,
    ) -> None:
        client = next(client for skill_name, client in self.clients if skill_name == "chembl-skill")
        base_url = "https://www.ebi.ac.uk/chembl/api/data"
        redirect = Mock()
        redirect.url = "https://www.ebi.ac.uk/chebi/backend/api/public/compound/CHEBI:15377"
        response = Mock()
        response.status_code = 200
        response.headers = {"content-type": "application/json"}
        response.url = f"{base_url}/molecule/CHEMBL25.json"
        response.history = [redirect]
        response.text = '{"molecule_chembl_id": "CHEMBL25"}'
        response.content = response.text.encode("utf-8")
        response.json.return_value = {"molecule_chembl_id": "CHEMBL25"}
        session = Mock()
        session.request.return_value = response

        with patch.object(client.requests, "Session", return_value=session):
            output = client.execute({"base_url": base_url, "path": "molecule/CHEMBL25.json"})

        self.assertFalse(output["ok"])
        self.assertEqual("invalid_response", output["error"]["code"])
        self.assertNotIn("sources", output)
        self.assertNotIn("checked_sources", output)
        session.close.assert_called_once_with()

    def test_real_response_without_final_url_fails_closed(self) -> None:
        skill_name, client = self.clients[0]
        base_url = _registered_base_url(skill_name)
        response = client.requests.Response()
        response.status_code = 200
        response.headers = {"content-type": "application/json"}
        response._content = b'{"results": [{"id": "record"}]}'
        response.url = None
        session = Mock()
        session.request.return_value = response

        with patch.object(client.requests, "Session", return_value=session):
            output = client.execute({"base_url": base_url, "path": "records"})

        self.assertFalse(output["ok"])
        self.assertEqual("invalid_response", output["error"]["code"])
        self.assertNotIn("sources", output)
        session.close.assert_called_once_with()


if __name__ == "__main__":
    unittest.main()
