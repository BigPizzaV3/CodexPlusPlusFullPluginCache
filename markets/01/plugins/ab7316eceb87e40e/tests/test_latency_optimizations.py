"""Regression coverage for measured multi-request life-sciences hot paths."""

from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import tempfile
import unittest
from pathlib import Path
from typing import Any
from unittest.mock import MagicMock, Mock, patch

PLUGIN_ROOT = Path(__file__).resolve().parents[1]


def _load_module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


HEATMAP = _load_module(
    "latency_opentargets_disease_heatmap",
    PLUGIN_ROOT / "skills" / "opentargets-skill" / "scripts" / "opentargets_disease_heatmap.py",
)
GENEBASS = _load_module(
    "latency_genebass_gene_burden",
    PLUGIN_ROOT / "skills" / "genebass-gene-burden-skill" / "scripts" / "genebass_gene_burden.py",
)


def _heatmap_response(disease_id: str, raw: bytes) -> Mock:
    response = Mock()
    response.content = raw
    response.json.return_value = {
        "data": {
            "target": {
                "id": "ENSG00000186868",
                "approvedSymbol": "MAPT",
                "associatedDiseases": {
                    "count": 2,
                    "rows": [
                        {
                            "disease": {"id": disease_id, "name": "Asthma"},
                            "datasourceScores": [{"id": "ot_genetics_portal", "score": 0.8}],
                        }
                    ],
                },
            }
        }
    }
    return response


class OpenTargetsHeatmapLatencyTests(unittest.TestCase):
    @patch.object(HEATMAP.requests, "Session")
    def test_pages_reuse_one_session_and_preserve_exact_raw_bytes(self, factory) -> None:
        session = factory.return_value
        session.post.side_effect = [
            _heatmap_response("EFO_0000311", b'{"page": 1}\r\n'),
            _heatmap_response("EFO_0000408", b'{"page": 2}\n'),
        ]

        with tempfile.TemporaryDirectory() as temporary_directory:
            raw_path = Path(temporary_directory) / "diseases.json"
            result = HEATMAP.execute(
                {
                    "ensembl_id": "ENSG00000186868",
                    "page_size": 1,
                    "max_pages": 2,
                    "save_raw": True,
                    "raw_output_path": str(raw_path),
                }
            )

            self.assertTrue(result["ok"])
            self.assertEqual(2, result["summary"]["pages_fetched"])
            self.assertEqual(2, session.post.call_count)
            self.assertEqual(b'{"page": 1}\r\n', raw_path.read_bytes())
            self.assertEqual(
                b'{"page": 2}\n',
                raw_path.with_name("diseases.page-2.json").read_bytes(),
            )
            self.assertTrue(result["sources"][0]["supports_claim"])

        factory.assert_called_once_with()
        session.close.assert_called_once_with()
        for invocation in session.post.call_args_list:
            self.assertEqual(60, invocation.kwargs["timeout"])

    @patch.object(HEATMAP.requests, "Session")
    def test_network_failure_closes_session_without_leaking_request(self, factory) -> None:
        session = factory.return_value
        session.post.side_effect = HEATMAP.requests.Timeout("query=PRIVATE&api_key=SECRET")

        result = HEATMAP.execute({"ensembl_id": "ENSG00000186868"})

        self.assertFalse(result["ok"])
        self.assertEqual("network_error", result["error"]["code"])
        self.assertNotIn("PRIVATE", json.dumps(result))
        self.assertNotIn("SECRET", json.dumps(result))
        session.close.assert_called_once_with()


class GeneBassLatencyTests(unittest.TestCase):
    def _run_main(self, payload: dict[str, Any]) -> tuple[int, dict[str, Any]]:
        output = io.StringIO()
        with patch("sys.stdin", io.StringIO(json.dumps(payload))):
            with contextlib.redirect_stdout(output):
                status = GENEBASS.main()
        return status, json.loads(output.getvalue())

    @staticmethod
    def _session(factory: MagicMock) -> MagicMock:
        session = MagicMock()
        factory.return_value.__enter__.return_value = session
        return session

    @patch.object(GENEBASS.requests, "Session")
    def test_gene_and_phenotype_requests_share_one_session(self, factory) -> None:
        session = self._session(factory)
        gene_response = Mock(status_code=200)
        gene_response.json.return_value = {
            "gene": {"gene_id": "ENSG00000173531", "symbol": "MST1"},
            "phewas": [
                {
                    "trait_type": "continuous",
                    "phenocode": "trait",
                    "pheno_sex": "both",
                    "coding": "",
                    "modifier": "",
                    "Pvalue": 0.01,
                }
            ],
        }
        metadata_response = Mock(status_code=200)
        metadata_response.json.return_value = [
            {"analysis_id": "continuous-trait-both--", "description": "Example trait"}
        ]
        session.get.side_effect = [gene_response, metadata_response]

        status, result = self._run_main({"ensembl_gene_id": "ENSG00000173531", "max_results": 1})

        self.assertEqual(0, status)
        self.assertTrue(result["ok"])
        self.assertEqual(2, session.get.call_count)
        self.assertEqual("Example trait", result["associations"][0]["phenotype_description"])
        self.assertTrue(result["sources"][0]["supports_claim"])
        factory.assert_called_once_with()
        factory.return_value.__exit__.assert_called_once()
        for invocation in session.get.call_args_list:
            self.assertEqual(GENEBASS.DEFAULT_TIMEOUT_S, invocation.kwargs["timeout"])

    @patch.object(GENEBASS.requests, "Session")
    def test_missing_gene_closes_session_without_fetching_metadata(self, factory) -> None:
        session = self._session(factory)
        session.get.return_value = Mock(status_code=404)

        status, result = self._run_main({"ensembl_gene_id": "ENSG00000173531"})

        self.assertEqual(0, status)
        self.assertEqual(0, result["association_count"])
        self.assertNotIn("sources", result)
        session.get.assert_called_once()
        factory.return_value.__exit__.assert_called_once()

    @patch.object(GENEBASS.requests, "Session")
    def test_metadata_failure_preserves_evidence_and_redacts_error(self, factory) -> None:
        session = self._session(factory)
        response = Mock(status_code=200)
        response.json.return_value = {
            "gene": {"gene_id": "ENSG00000173531"},
            "phewas": [{"trait_type": "continuous", "phenocode": "trait", "Pvalue": 0.1}],
        }
        session.get.side_effect = [
            response,
            GENEBASS.requests.Timeout("query=PRIVATE&api_key=SECRET"),
        ]

        status, result = self._run_main({"ensembl_gene_id": "ENSG00000173531"})

        self.assertEqual(0, status)
        self.assertTrue(result["sources"][0]["supports_claim"])
        self.assertIn("Timeout", result["warnings"][0])
        self.assertNotIn("PRIVATE", json.dumps(result))
        self.assertNotIn("SECRET", json.dumps(result))
        factory.return_value.__exit__.assert_called_once()


if __name__ == "__main__":
    unittest.main()
