"""Exhaustive database evidence, URL-safety, raw-output, and skill coverage."""

from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from typing import Any
from unittest.mock import Mock, patch
from urllib.parse import quote

PLUGIN_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = PLUGIN_ROOT / "skills"
REGISTRY_PATH = PLUGIN_ROOT / "references" / "source-links.json"


def _load_module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


CONTRACT = _load_module(
    "database_source_contract_tests",
    PLUGIN_ROOT / "scripts" / "database_source_contract.py",
)


_EXAMPLE_IDENTIFIERS = {
    "UniProt accession": "P04637",
    "variant": "10-112998590-C-T",
    "phenotype": "T2D",
    "DOI": "10.1093/nar/gkr1184",
    "study accession": "GCST90000001",
    "collection ID": "f2e24523-2222-4444-8888-123456789012",
    "ChEBI ID": "CHEBI:15377",
    "compound ID": "CHEMBL25",
    "target ID": "CHEMBL203",
    "variant ID": "12345",
    "evidence ID": "67890",
    "NCT ID": "NCT01234567",
    "numeric ClinVar Variation ID": "VCV000013080",
    "RefSNP ID": "rs7903146",
    "ENCODE accession": "ENCSR000AAA",
    "stable Ensembl ID": "ENSG00000141510",
    "gene ID": "ENSG00000141510",
    "association accession": "123456",
    "gene symbol or Ensembl gene ID": "TP53",
    "MetaboLights study accession": "MTBLS1",
    "analysis accession": "MGYA000001",
    "sample accession": "SAMN00000001",
    "NCBI Gene ID": "7157",
    "genome accession": "GCF_000001405.40",
    "PMID": "22966082",
    "PMCID": "PMC3257301",
    "GEO accession": "GSE60450",
    "disease ID": "EFO_0000311",
    "chemical ID": "PA451906",
    "PRIDE project accession": "PXD000001",
    "ProteomeXchange accession": "PXD000001",
    "compound CID": "2244",
    "substance SID": "12345",
    "assay AID": "67890",
    "GO term": "GO:0008150",
    "PDB ID": "4OBE",
    "Reactome stable ID": "R-HSA-6802949",
    "Rhea numeric ID": "RHEA:12345",
    "RNAcentral ID": "URS0000000001",
    "STRING protein identifier": "9606.ENSP00000269305",
    "UniProtKB accession": "P04637",
    "UniRef cluster": "UniRef90_P04637",
    "UniParc accession": "UPI0000000001",
}

_SKILL_IDENTIFIER_OVERRIDES = {
    ("biostudies-arrayexpress-skill", "study accession"): "E-MTAB-1234",
    ("gwas-catalog-skill", "variant"): "rs7903146",
    ("mgnify-skill", "study accession"): "MGYS000001",
    ("opentargets-skill", "target ID"): "ENSG00000141510",
    ("pharmgkb-skill", "gene ID"): "PA12345",
    ("pharmgkb-skill", "variant ID"): "PA23456",
}


def _example_identifier(skill_name: str, identifier_type: str) -> str:
    return _SKILL_IDENTIFIER_OVERRIDES.get(
        (skill_name, identifier_type), _EXAMPLE_IDENTIFIERS[identifier_type]
    )


class ExhaustiveCoverageTests(unittest.TestCase):
    def test_plugin_covers_all_44_skills_exactly(self) -> None:
        skill_names = {path.parent.name for path in SKILLS_ROOT.glob("*/SKILL.md")}
        registry_names = set(json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))["skills"])
        self.assertEqual(44, len(skill_names))
        self.assertEqual(skill_names, registry_names)

    def test_complete_contract_validator(self) -> None:
        validator = _load_module(
            "database_source_contract_validator_tests",
            PLUGIN_ROOT / "scripts" / "validate_source_contract.py",
        )
        errors = validator.validate()
        self.assertFalse(errors, "; ".join(errors[:5]))

    def test_every_runtime_client_applies_the_shared_contract(self) -> None:
        for skill in sorted(SKILLS_ROOT.glob("*/SKILL.md")):
            clients = [
                path
                for path in (skill.parent / "scripts").glob("*.py")
                if not path.name.startswith("test_") and path.name != "variant_resolution.py"
            ]
            self.assertTrue(clients, skill.parent.name)
            for client in clients:
                with self.subTest(skill=skill.parent.name, client=client.name):
                    self.assertTrue(
                        "apply_source_contract" in client.read_text(encoding="utf-8"),
                        f"{skill.parent.name}/{client.name} does not apply the source contract",
                    )

    def test_variant_helpers_delegate_to_one_shared_implementation(self) -> None:
        shared_helper = PLUGIN_ROOT / "scripts" / "database_variant_resolution.py"
        local_helpers = sorted(SKILLS_ROOT.glob("*/scripts/variant_resolution.py"))
        self.assertTrue(shared_helper.is_file())
        self.assertTrue(local_helpers)
        for helper in local_helpers:
            with self.subTest(skill=helper.parents[1].name):
                self.assertIn("database_variant_resolution", helper.read_text(encoding="utf-8"))
                self.assertLess(helper.stat().st_size, shared_helper.stat().st_size)

    def test_all_rest_clients_distinguish_evidence_from_empty_results(self) -> None:
        registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))["skills"]
        clients = sorted(SKILLS_ROOT.glob("*/scripts/rest_request.py"))
        expected_rest_skills = {
            skill_name
            for skill_name, entry in registry.items()
            if entry.get("request_url_prefixes")
        }
        self.assertEqual(expected_rest_skills, {path.parents[1].name for path in clients})
        for index, path in enumerate(clients):
            skill_name = path.parents[1].name
            module = _load_module(f"generic_database_contract_client_{index}", path)
            base_url = registry[skill_name]["request_url_prefixes"][0].rstrip("/")
            first_mapping = next(iter(registry[skill_name]["record_url_templates"]), None)
            record = {"description": "returned source evidence"}
            if first_mapping is not None:
                record[first_mapping["identifier_fields"][0]] = _example_identifier(
                    skill_name, first_mapping["identifier_type"]
                )
            for records in ([record], []):
                with self.subTest(skill=skill_name, evidence=bool(records)):
                    response = Mock()
                    response.status_code = 200
                    response.headers = {"content-type": "application/json"}
                    response.url = f"{base_url}/records?query=private&api_key=secret"
                    response.text = json.dumps({"results": records})
                    response.json.return_value = {"results": records}
                    session = Mock()
                    session.request.return_value = response
                    with patch.object(module.requests, "Session", return_value=session):
                        output = module.execute(
                            {
                                "base_url": base_url,
                                "path": "records",
                                "record_path": "results",
                            }
                        )
                    if records:
                        self.assertTrue(output["sources"][0]["supports_claim"])
                        self.assertEqual(
                            registry[skill_name]["source_name"],
                            output["sources"][0]["name"],
                        )
                        if first_mapping is not None:
                            self.assertIn("canonical_url", output["records"][0])
                    else:
                        self.assertNotIn("sources", output)
                        self.assertFalse(output["checked_sources"][0]["supports_claim"])
                    self.assertNotIn("private", json.dumps(output))
                    self.assertNotIn("secret", json.dumps(output))

    def test_every_registered_url_template_is_constructible_and_escaped(self) -> None:
        registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))["skills"]
        count = 0
        for skill_name, entry in registry.items():
            for mapping in entry["record_url_templates"]:
                kind = mapping["identifier_type"]
                with self.subTest(skill=skill_name, identifier_type=kind):
                    identifier = _example_identifier(skill_name, kind)
                    field = mapping["identifier_fields"][0]
                    normalized = identifier
                    if mapping.get("transform") == "strip_clinvar_vcv":
                        normalized = "13080"
                    elif mapping.get("transform") == "strip_rhea_prefix":
                        normalized = "12345"
                    expected = mapping["template"].replace(
                        "{id}", quote(normalized, safe="/" if kind == "DOI" else "")
                    )
                    actual = CONTRACT.canonical_record_url(
                        skill_name,
                        {field: identifier},
                        identifier_type=kind,
                    )
                    self.assertEqual(expected, actual)
                    count += 1
        self.assertEqual(59, count)

    def test_unsupported_and_ambiguous_mappings_never_invent_urls(self) -> None:
        cases = (
            ("alphafold-skill", {"accession": "NOT_A_UNIPROT"}),
            ("bindingdb-skill", {"id": "12345"}),
            ("cellxgene-skill", {"collection_id": "NOT_A_UUID"}),
            ("civic-skill", {"variant_id": "rs7903146"}),
            ("chembl-skill", {"target_chembl_id": "ENSG00000141510"}),
            ("chembl-skill", {"id": "CHEMBL25", "pref_name": "ASPIRIN"}),
            ("efo-ontology-skill", {"id": "EFO_0000311"}),
            ("encode-skill", {"accession": "INVALID"}),
            ("ensembl-skill", {"ensembl_id": "ENSNOTREAL"}),
            ("gwas-catalog-skill", {"study_accession": "INVALID"}),
            ("gwas-catalog-skill", {"association_accession": "totally_invalid"}),
            ("human-protein-atlas-skill", {"gene_symbol": "not-a-real-gene"}),
            ("ncbi-datasets-skill", {"assembly_accession": "INVALID"}),
            ("opentargets-skill", {"target_id": "CHEMBL203"}),
            ("string-skill", {"preferredName": "TP53"}),
            ("unknown-skill", {"id": "12345"}),
            ("uniprot-skill", {"accession": "../../secrets"}),
            ("uniprot-skill", {"accession": "INVALID"}),
            ("ncbi-entrez-skill", {"id": "7157"}),
            ("ncbi-entrez-skill", {"doi": "10.1093/../secret"}),
            ("ncbi-entrez-skill", {"geo_accession": "GSEnot-a-real123"}),
            ("clinicaltrials-skill", {"nctId": "NCT123"}),
            ("clinvar-variation-skill", {"variation_id": "VCVsecret"}),
        )
        for skill_name, record in cases:
            with self.subTest(skill=skill_name, record=record):
                self.assertIsNone(CONTRACT.canonical_record_url(skill_name, record))

    def test_database_context_disambiguates_scalar_entrez_identifiers(self) -> None:
        self.assertEqual(
            "https://pubmed.ncbi.nlm.nih.gov/22966082/",
            CONTRACT.canonical_record_url(
                "ncbi-entrez-skill", {"id": "22966082"}, database="pubmed"
            ),
        )
        self.assertEqual(
            "https://www.ncbi.nlm.nih.gov/gene/7157",
            CONTRACT.canonical_record_url("ncbi-entrez-skill", {"id": "7157"}, database="gene"),
        )
        self.assertEqual(
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC3257301/",
            CONTRACT.canonical_record_url("ncbi-entrez-skill", {"id": "3257301"}, database="pmc"),
        )
        output = CONTRACT.apply_source_contract(
            {"ok": True, "database": "pubmed", "records": ["22966082"]},
            "ncbi-entrez-skill",
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi",
        )
        self.assertEqual(["22966082"], output["records"])
        self.assertEqual(
            "https://pubmed.ncbi.nlm.nih.gov/22966082/",
            output["sources"][0]["canonical_url"],
        )


class SourceSafetyTests(unittest.TestCase):
    def test_registered_request_scopes_come_from_the_skill_registry(self) -> None:
        registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))["skills"]
        rest_skills = {
            path.parents[1].name for path in SKILLS_ROOT.glob("*/scripts/rest_request.py")
        }
        self.assertEqual(
            {name for name, entry in registry.items() if entry.get("request_url_prefixes")},
            rest_skills,
        )
        for skill_name in sorted(rest_skills):
            prefixes = registry[skill_name].get("request_url_prefixes")
            self.assertIsInstance(prefixes, list)
            self.assertTrue(prefixes)
            for url in prefixes:
                with self.subTest(skill=skill_name, url=url):
                    self.assertTrue(CONTRACT.is_registered_source_url(skill_name, url))

    def test_registered_base_urls_require_the_skill_host_and_path_scope(self) -> None:
        accepted = (
            ("chembl-skill", "https://www.ebi.ac.uk/chembl/api/data"),
            ("chembl-skill", "HTTPS://WWW.EBI.AC.UK/chembl/api/data/"),
            ("chebi-skill", "https://www.ebi.ac.uk"),
            ("chebi-skill", "https://www.ebi.ac.uk/chebi/backend/api/public"),
        )
        rejected = (
            ("chembl-skill", "https://www.ebi.ac.uk/chebi/backend/api/public"),
            ("chebi-skill", "https://www.ebi.ac.uk/chembl/api/data"),
            ("chembl-skill", "https://www.ebi.ac.uk/chembl/api/data?query=private"),
            ("chembl-skill", "https://www.ebi.ac.uk/chembl/api/data#fragment"),
            ("chembl-skill", "https://www.ebi.ac.uk:443/chembl/api/data"),
            ("missing-skill", "https://www.ebi.ac.uk/chembl/api/data"),
        )
        for skill_name, url in accepted:
            with self.subTest(accepted=True, skill=skill_name, url=url):
                self.assertTrue(CONTRACT.is_registered_source_base_url(skill_name, url))
        for skill_name, url in rejected:
            with self.subTest(accepted=False, skill=skill_name, url=url):
                self.assertFalse(CONTRACT.is_registered_source_base_url(skill_name, url))

    def test_registered_source_urls_allow_only_exact_https_scopes(self) -> None:
        accepted = (
            ("alphafold-skill", "HTTPS://ALPHAFOLD.EBI.AC.UK/api"),
            ("rcsb-pdb-skill", "https://data.rcsb.org/rest/v1"),
            ("rcsb-pdb-skill", "https://search.rcsb.org/rcsbsearch/v2"),
            ("chembl-skill", "https://www.ebi.ac.uk/chembl/api/data/molecule.json"),
        )
        rejected = (
            ("alphafold-skill", "https://example.org/results"),
            ("alphafold-skill", "https://ebi.ac.uk/results"),
            ("chembl-skill", "https://alphafold.ebi.ac.uk/api/prediction/P04637"),
            ("chembl-skill", "https://www.ebi.ac.uk/chebi/backend/api/public"),
            ("alphafold-skill", "https://alphafold.ebi.ac.uk.evil.example/results"),
            ("alphafold-skill", "http://alphafold.ebi.ac.uk/results"),
            ("alphafold-skill", "https://alphafold.ebi.ac.uk:443/api"),
            ("alphafold-skill", "https://alphafold.ebi.ac.uk:/api"),
            ("alphafold-skill", "https://alphafold.ebi.ac.uk:444/results"),
            ("alphafold-skill", "https://alphafold.ebi.ac.uk:not-a-port/api"),
            ("alphafold-skill", "https://alphafold.ebi.ac.uk./api"),
            ("alphafold-skill", "https://user:secret@alphafold.ebi.ac.uk/results"),
            ("alphafold-skill", "https://alphafold.ebi.ac.uk\\@evil.example/results"),
            ("missing-skill", "https://alphafold.ebi.ac.uk/results"),
        )
        for skill_name, url in accepted:
            with self.subTest(accepted=True, skill=skill_name, url=url):
                self.assertTrue(CONTRACT.is_registered_source_url(skill_name, url))
        for skill_name, url in rejected:
            with self.subTest(accepted=False, skill=skill_name, url=url):
                self.assertFalse(CONTRACT.is_registered_source_url(skill_name, url))
        for url in (
            "https://alphafold.ebi.ac.uk:443/api",
            "https://alphafold.ebi.ac.uk:/api",
            "https://alphafold.ebi.ac.uk:not-a-port/api",
            "https://alphafold.ebi.ac.uk./api",
        ):
            with self.subTest(origin=False, url=url):
                self.assertFalse(CONTRACT.is_registered_source_origin("alphafold-skill", url))

    def test_url_redacts_credentials_secrets_queries_sequences_and_fragments(
        self,
    ) -> None:
        raw = (
            "https://alice:password@example.org/records?"
            "id=P04637&api_key=secret&access_token=hidden&sig=signed&"
            "query=private-patient&term=private-search&sequence=ATGC&email=person%40example.org"
            "#access_token=fragment-secret"
        )
        sanitized = CONTRACT.sanitize_request_url(raw)
        self.assertIsNotNone(sanitized)
        self.assertTrue(sanitized.startswith("https://example.org/records?"))
        self.assertIn("id=P04637", sanitized)
        for private in (
            "alice",
            "password",
            "secret",
            "hidden",
            "signed",
            "private-patient",
            "private-search",
            "ATGC",
            "person",
            "fragment",
            "#",
        ):
            with self.subTest(private=private):
                self.assertNotIn(private, sanitized)
        self.assertEqual(7, sanitized.count("REDACTED"))

    def test_invalid_request_urls_are_not_promoted(self) -> None:
        for value in (
            None,
            "",
            "ftp://example.org/data",
            "file:///tmp/secret",
            "../record",
        ):
            with self.subTest(value=value):
                self.assertIsNone(CONTRACT.sanitize_request_url(value))

    def test_camel_case_secrets_patient_queries_and_prompts_are_redacted(self) -> None:
        sensitive_keys = (
            "accessToken",
            "authToken",
            "bearerToken",
            "refreshToken",
            "clientSecret",
            "queryText",
            "searchTerm",
            "filterQuery",
            "sequenceData",
            "patientQuery",
            "prompt",
            "oauthAccessToken",
            "APIKey",
            "sessionid",
            "PHPSESSID",
            "sid",
            "sas",
            "subjectId",
            "diagnosis",
            "expr",
            "expression",
            "q0",
            "q1",
            "terms",
            "WebEnv",
        )
        for index, key in enumerate(sensitive_keys):
            sentinel = f"PRIVATE_VALUE_{index}"
            with self.subTest(key=key):
                sanitized = CONTRACT.sanitize_request_url(
                    f"https://example.org/api?id=7157&{key}={sentinel}"
                )
                self.assertNotIn(sentinel, sanitized)
                self.assertIn("REDACTED", sanitized)
                self.assertIn("id=7157", sanitized)

    def test_evidence_records_receive_only_supported_authoritative_urls(self) -> None:
        output = CONTRACT.apply_source_contract(
            {
                "ok": True,
                "record_count_returned": 1,
                "records": [{"primaryAccession": "P04637", "proteinDescription": "p53"}],
            },
            "uniprot-skill",
            "https://rest.uniprot.org/uniprotkb/search?query=private&api_key=secret",
        )
        canonical = "https://www.uniprot.org/uniprotkb/P04637/entry"
        self.assertEqual(canonical, output["records"][0]["canonical_url"])
        self.assertEqual(canonical, output["sources"][0]["canonical_url"])
        self.assertTrue(output["sources"][0]["supports_claim"])
        self.assertEqual("evidence", output["sources"][0]["kind"])
        self.assertNotIn("private", json.dumps(output["sources"]))
        self.assertNotIn("secret", json.dumps(output["sources"]))

    def test_same_record_collects_every_supported_canonical_mapping(self) -> None:
        output = CONTRACT.apply_source_contract(
            {
                "ok": True,
                "records": [
                    {
                        "molecule_chembl_id": "CHEMBL25",
                        "target_chembl_id": "CHEMBL203",
                        "canonical_url": "https://attacker.example/compound/CHEMBL25",
                        "canonical_urls": [
                            "javascript:alert('unsafe')",
                            "https://attacker.example/target/CHEMBL203",
                        ],
                    }
                ],
            },
            "chembl-skill",
            "https://www.ebi.ac.uk/chembl/api/data/activity.json",
        )
        compound = "https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL25"
        target = "https://www.ebi.ac.uk/chembl/explore/target/CHEMBL203"
        record = output["records"][0]
        self.assertEqual(compound, record["canonical_url"])
        self.assertEqual([compound, target], record["canonical_urls"])
        self.assertEqual(compound, output["sources"][0]["canonical_url"])
        self.assertEqual([compound, target], output["sources"][0]["canonical_urls"])
        self.assertEqual(
            compound,
            CONTRACT.canonical_record_url("chembl-skill", record),
        )

    def test_unsupported_sources_keep_provenance_without_fake_record_urls(self) -> None:
        output = CONTRACT.apply_source_contract(
            {
                "ok": True,
                "summary": {
                    "affinity_nm": 42,
                    "canonical_url": "https://attacker.example/fake-record",
                    "canonical_urls": ["javascript:alert('unsafe')"],
                },
            },
            "bindingdb-skill",
            "https://bindingdb.org/api?query=private",
        )
        self.assertEqual("evidence", output["sources"][0]["kind"])
        self.assertNotIn("canonical_url", output["summary"])
        self.assertNotIn("canonical_urls", output["summary"])
        self.assertNotIn("canonical_url", output["sources"][0])
        self.assertNotIn("canonical_urls", output["sources"][0])
        self.assertIn("query=REDACTED", output["sources"][0]["request_url"])

    def test_canonical_only_payload_is_checked_after_reserved_fields_are_removed(self) -> None:
        output = CONTRACT.apply_source_contract(
            {
                "ok": True,
                "summary": {
                    "canonical_url": "https://attacker.example/fake-record",
                    "canonical_urls": ["javascript:alert('unsafe')"],
                },
            },
            "bindingdb-skill",
            "https://bindingdb.org/",
        )
        self.assertEqual({}, output["summary"])
        self.assertNotIn("sources", output)
        self.assertFalse(output["checked_sources"][0]["supports_claim"])
        self.assertEqual("empty", output["checked_sources"][0]["reason"])

    def test_reserved_canonical_fields_are_removed_beyond_annotation_limit(self) -> None:
        records = [{"description": f"row {index}"} for index in range(101)]
        records[100]["canonical_url"] = "https://attacker.example/fake-record"
        records[100]["canonical_urls"] = ["javascript:alert('unsafe')"]
        nested = records[100]
        for _ in range(8):
            nested["nested"] = {}
            nested = nested["nested"]
        nested["canonical_url"] = "https://attacker.example/deep-record"
        output = CONTRACT.apply_source_contract(
            {"ok": True, "records": records},
            "bindingdb-skill",
            "https://bindingdb.org/",
        )
        self.assertNotIn("canonical_url", output["records"][100])
        self.assertNotIn("canonical_urls", output["records"][100])
        nested = output["records"][100]
        for _ in range(8):
            nested = nested["nested"]
        self.assertNotIn("canonical_url", nested)

    def test_reserved_canonical_fields_are_removed_from_existing_sources(self) -> None:
        upstream = {
            "name": "Upstream",
            "url": "https://example.org/evidence",
            "kind": "evidence",
            "supports_claim": True,
            "canonical_url": "https://attacker.example/fake-record",
            "canonical_urls": ["javascript:alert('unsafe')"],
        }
        checked = {
            "name": "Checked",
            "url": "https://example.org/check",
            "kind": "checked",
            "supports_claim": False,
            "canonical_url": "https://attacker.example/fake-check",
            "canonical_urls": ["javascript:alert('unsafe')"],
        }
        output = CONTRACT.apply_source_contract(
            {
                "ok": True,
                "records": [{"primaryAccession": "P04637"}],
                "sources": [upstream],
                "checked_sources": [checked],
            },
            "uniprot-skill",
            "https://rest.uniprot.org/uniprotkb/P04637",
        )
        for item in (output["sources"][0], output["checked_sources"][0]):
            self.assertNotIn("canonical_url", item)
            self.assertNotIn("canonical_urls", item)
        self.assertEqual(
            "https://www.uniprot.org/uniprotkb/P04637/entry",
            output["sources"][-1]["canonical_url"],
        )

    def test_real_study_is_evidence_when_validation_metadata_is_empty(self) -> None:
        output = CONTRACT.apply_source_contract(
            {
                "ok": True,
                "summary": {
                    "isaInvestigation": {
                        "identifier": "MTBLS1",
                        "title": "Human metabolic study",
                    },
                    "validation": {"errors": [], "warnings": []},
                },
            },
            "metabolights-skill",
            "https://www.ebi.ac.uk/metabolights/ws/studies/MTBLS1",
        )

        self.assertEqual("evidence", output["sources"][0]["kind"])
        self.assertEqual(
            "https://www.ebi.ac.uk/metabolights/MTBLS1",
            output["summary"]["isaInvestigation"]["canonical_url"],
        )

    def test_clinpgx_record_ids_require_an_explicit_object_class(self) -> None:
        examples = (
            ("Gene", "PA128", "https://www.clinpgx.org/gene/PA128"),
            (
                "Variant",
                "PA166158545",
                "https://www.clinpgx.org/variant/PA166158545",
            ),
            ("Chemical", "PA449726", "https://www.clinpgx.org/chemical/PA449726"),
        )
        for object_class, identifier, expected in examples:
            with self.subTest(object_class=object_class):
                output = CONTRACT.apply_source_contract(
                    {
                        "ok": True,
                        "summary": {"data": {"objCls": object_class, "id": identifier}},
                    },
                    "pharmgkb-skill",
                    "https://api.clinpgx.org/v1/data/",
                )
                self.assertEqual(expected, output["summary"]["data"]["canonical_url"])
                self.assertEqual(expected, output["sources"][0]["canonical_url"])

        ambiguous = CONTRACT.apply_source_contract(
            {"ok": True, "summary": {"data": {"id": "PA128"}}},
            "pharmgkb-skill",
            "https://api.clinpgx.org/v1/data/",
        )
        self.assertNotIn("canonical_url", ambiguous["summary"]["data"])

    def test_rhea_sparql_accession_receives_a_validated_canonical_url(self) -> None:
        output = CONTRACT.apply_source_contract(
            {
                "ok": True,
                "records": [
                    {
                        "accession": {"type": "literal", "value": "RHEA:47148"},
                        "equation": {"type": "literal", "value": "A = B"},
                    }
                ],
            },
            "rhea-skill",
            "https://sparql.rhea-db.org/sparql?query=private",
        )

        expected = "https://www.rhea-db.org/rhea/47148"
        self.assertEqual(expected, output["records"][0]["canonical_url"])
        self.assertEqual(expected, output["sources"][0]["canonical_url"])
        self.assertNotIn("private", json.dumps(output["sources"]))

    def test_empty_metadata_connectivity_and_failures_are_not_evidence(self) -> None:
        cases = (
            ({"ok": True, "record_count_returned": 0, "records": []}, None, "empty"),
            ({"ok": True, "association_count": 0, "associations": []}, None, "empty"),
            ({"ok": True, "summary": {"variant": None}}, None, "empty"),
            (
                {"ok": True, "summary": {"status": "ok", "version": "1"}},
                None,
                "metadata",
            ),
            (
                {
                    "ok": True,
                    "summary": {"apiVersion": "1", "serviceStatus": "healthy"},
                },
                None,
                "metadata",
            ),
            ({"ok": True, "summary": {"schemaVersion": "1"}}, None, "metadata"),
            ({"ok": True, "summary": {"total": 0}}, None, "empty"),
            ({"ok": True, "summary": {"totalCount": 0}}, None, "empty"),
            (
                {
                    "ok": True,
                    "summary": {"response": [{"numResults": 0, "numTotalResults": 0}]},
                },
                None,
                "empty",
            ),
            (
                {
                    "ok": True,
                    "summary": {
                        "apiVersion": "v1",
                        "queryOptions": {"metadata": True, "limit": 1, "skip": 0},
                        "response": [{"numResults": 0, "numTotalResults": 0}],
                    },
                },
                None,
                "empty",
            ),
            (
                {"ok": True, "summary": {"pagination": {"count": 0, "next": None}}},
                None,
                "empty",
            ),
            (
                {"ok": True, "summary": {"pagination": {"cursor": "abc"}}},
                None,
                "metadata",
            ),
            (
                {"ok": True, "summary": {"meta": {"cursor": "abc"}}},
                None,
                "metadata",
            ),
            (
                {
                    "ok": True,
                    "summary": {"meta": {"clinvar_release_date": "2026-07-01"}},
                },
                None,
                "metadata",
            ),
            (
                {"ok": True, "summary": {"data": {"__typename": "Query"}}},
                None,
                "metadata",
            ),
            (
                {
                    "ok": True,
                    "summary": {"data": None, "extensions": {"tracing": {"duration": 23}}},
                },
                None,
                "empty",
            ),
            ({"ok": True, "summary": {"healthCheck": True}}, None, "metadata"),
            (
                {"ok": True, "summary": {"endpoint": "status", "reachable": True}},
                None,
                "metadata",
            ),
            (
                {
                    "ok": True,
                    "summary": {"__type": {"name": "Gene", "fields": [{"name": "id"}]}},
                },
                None,
                "metadata",
            ),
            ({"ok": True, "summary": {"__typename": "Query"}}, None, "metadata"),
            (
                {"ok": True, "summary": {"data": {"__typename": "Query"}}},
                None,
                "metadata",
            ),
            (
                {
                    "ok": True,
                    "summary": {"meta": {"clinvar_release_date": "2026-07-01"}},
                },
                None,
                "metadata",
            ),
            (
                {
                    "ok": True,
                    "summary": {
                        "data": None,
                        "extensions": {"tracing": {"duration": 23}},
                    },
                },
                None,
                "empty",
            ),
            (
                {"ok": True, "endpoint": "egquery", "summary": {"pubmed_count": 42}},
                None,
                "metadata",
            ),
            (
                {"ok": True, "endpoint": "espell", "summary": {"corrected": "BRCA1"}},
                None,
                "metadata",
            ),
            (
                {
                    "ok": True,
                    "path": "fields",
                    "records": [{"name": "gene", "type": "string"}],
                },
                None,
                "metadata",
            ),
            (
                {
                    "ok": True,
                    "path": "meta/species/list",
                    "record_count_returned": 1,
                    "records": [{"taxonomyId": 9606, "taxonomyCommonName": "Human"}],
                },
                None,
                "metadata",
            ),
            (
                {
                    "ok": True,
                    "path": "healthz",
                    "summary": {"ok": True, "uptime": 123},
                },
                None,
                "metadata",
            ),
            (
                {
                    "ok": True,
                    "summary": {
                        "capabilities": ["search", "download"],
                        "version": "1.0",
                    },
                },
                None,
                "metadata",
            ),
            (
                {"ok": True, "summary": {"records": [], "head": {"vars": ["x"]}}},
                None,
                "empty",
            ),
            ({"ok": True, "summary": {"gene": "TP53"}}, "connectivity", "connectivity"),
            (
                {"ok": True, "action": "metadata", "records": [{"name": "schema"}]},
                None,
                "metadata",
            ),
        )
        for payload, mode, reason in cases:
            with self.subTest(payload=payload, mode=mode):
                result = CONTRACT.apply_source_contract(
                    payload, "uniprot-skill", "https://rest.uniprot.org/", mode=mode
                )
                self.assertNotIn("sources", result)
                self.assertFalse(result["checked_sources"][0]["supports_claim"])
                self.assertEqual(reason, result["checked_sources"][0]["reason"])
        failure = {"ok": False, "error": {"code": "network_error", "message": "failed"}}
        self.assertIs(
            failure,
            CONTRACT.apply_source_contract(failure, "uniprot-skill", "https://example.org/"),
        )
        self.assertNotIn("sources", failure)
        self.assertNotIn("checked_sources", failure)

    def test_nested_numeric_string_zero_counts_are_empty(self) -> None:
        for count in ("0", "  0  ", "+0", "-0", "00", "0.0", "0e12"):
            with self.subTest(count=count):
                output = CONTRACT.apply_source_contract(
                    {
                        "ok": True,
                        "summary": {
                            "eSearchResult": {"Count": count, "IdList": ""},
                        },
                    },
                    "ncbi-entrez-skill",
                    "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi",
                )
                self.assertNotIn("sources", output)
                self.assertEqual("empty", output["checked_sources"][0]["reason"])

    def test_collection_shapes_metadata_wrappers_and_deep_records(self) -> None:
        for value in ("malformed", 7):
            with self.subTest(malformed_records=value):
                output = CONTRACT.apply_source_contract(
                    {"ok": True, "records": value},
                    "uniprot-skill",
                    "https://rest.uniprot.org/uniprotkb/search",
                )
                self.assertNotIn("sources", output)
                self.assertEqual("empty", output["checked_sources"][0]["reason"])

        for value in ([{"primaryAccession": "P04637"}], {"primaryAccession": "P04637"}):
            with self.subTest(valid_records=value):
                output = CONTRACT.apply_source_contract(
                    {"ok": True, "records": value},
                    "uniprot-skill",
                    "https://rest.uniprot.org/uniprotkb/P04637",
                )
                self.assertTrue(output["sources"][0]["supports_claim"])

        entrez = CONTRACT.apply_source_contract(
            {
                "ok": True,
                "database": "pubmed",
                "summary": {"Count": "0", "IdList": "22966082"},
            },
            "ncbi-entrez-skill",
        )
        self.assertTrue(entrez["sources"][0]["supports_claim"])

        for wrapper in ("schema", "__typename", "cursor", "meta"):
            with self.subTest(metadata_wrapper=wrapper):
                output = CONTRACT.apply_source_contract(
                    {
                        "ok": True,
                        "summary": {wrapper: {"records": [{"primaryAccession": "P04637"}]}},
                    },
                    "uniprot-skill",
                )
                self.assertNotIn("sources", output)
                self.assertEqual("metadata", output["checked_sources"][0]["reason"])

        deep: dict[str, Any] = {"records": [{"primaryAccession": "P04637"}]}
        for index in range(10):
            deep = {f"wrapper_{index}": deep}
        output = CONTRACT.apply_source_contract(
            {"ok": True, "summary": {"Count": "0", "payload": deep}},
            "uniprot-skill",
        )
        self.assertTrue(output["sources"][0]["supports_claim"])

        cycle: dict[str, Any] = {}
        cycle["self"] = cycle
        self.assertEqual("empty", CONTRACT._summary_mode(cycle))

    def test_record_collections_suppress_only_structural_metadata(self) -> None:
        metadata_only = (
            {"records": [{"__typename": "Gene"}]},
            {"records": [{"__type": {"name": "Gene", "fields": [{"name": "id"}]}}]},
            {"summary": {"results": [{"schema": "v1"}]}},
            {"summary": {"items": [{"extensions": {"tracing": {"duration": 23}}}]}},
            {
                "records": [
                    {
                        "cursor": "next-page",
                        "meta": {"page": 1},
                        "metadata": {"version": "v1"},
                    }
                ]
            },
            {"records": [{"payload": [{"metadata": {"schema": "v1"}}]}]},
            {"records": [{"data": None}]},
        )
        for payload in metadata_only:
            with self.subTest(metadata_only=payload):
                output = CONTRACT.apply_source_contract(
                    {"ok": True, **payload},
                    "uniprot-skill",
                    "https://rest.uniprot.org/uniprotkb/search",
                )
                self.assertNotIn("sources", output)
                self.assertFalse(output["checked_sources"][0]["supports_claim"])
                self.assertEqual("empty", output["checked_sources"][0]["reason"])

        evidence_bearing = (
            {"records": [{"__typename": "Protein", "primaryAccession": "P04637"}]},
            {
                "summary": {
                    "results": [
                        {
                            "schema": "v1",
                            "record": {"primaryAccession": "P04637"},
                        }
                    ]
                }
            },
            {
                "summary": {
                    "items": [
                        {
                            "extensions": {"tracing": {"duration": 23}},
                            "data": {"records": [{"primaryAccession": "P04637"}]},
                        }
                    ]
                }
            },
        )
        for payload in evidence_bearing:
            with self.subTest(evidence_bearing=payload):
                output = CONTRACT.apply_source_contract(
                    {"ok": True, **payload},
                    "uniprot-skill",
                    "https://rest.uniprot.org/uniprotkb/P04637",
                )
                self.assertTrue(output["sources"][0]["supports_claim"])
                self.assertNotIn("checked_sources", output)

        cycle: dict[str, Any] = {}
        cycle["metadata"] = [cycle]
        self.assertFalse(CONTRACT._has_collection_value([cycle]))
        cycle["record"] = {"primaryAccession": "P04637"}
        self.assertTrue(CONTRACT._has_collection_value([cycle]))

    def test_http_200_diagnostics_are_not_evidence_but_real_sibling_records_are(self) -> None:
        diagnostic_cases = (
            ({"error": "not found"}, "failure"),
            (
                {
                    "errors": [
                        {
                            "message": "not found",
                            "details": {"code": "missing", "retryable": False},
                        }
                    ]
                },
                "failure",
            ),
            ({"warning": "partial response"}, "metadata"),
            (
                {"warnings": ["partial response", {"message": "retry later"}]},
                "metadata",
            ),
            (
                {"messages": ["no matching records", {"message": "try another query"}]},
                "metadata",
            ),
            (
                {
                    "payload": {
                        "errors": [
                            {
                                "message": "not found",
                                "details": {"records": [{"primaryAccession": "P04637"}]},
                            }
                        ]
                    }
                },
                "failure",
            ),
        )
        for summary, reason in diagnostic_cases:
            with self.subTest(summary=summary):
                output = CONTRACT.apply_source_contract(
                    {"ok": True, "status_code": 200, "summary": summary},
                    "uniprot-skill",
                    "https://rest.uniprot.org/uniprotkb/search",
                )
                self.assertNotIn("sources", output)
                self.assertFalse(output["checked_sources"][0]["supports_claim"])
                self.assertEqual(reason, output["checked_sources"][0]["reason"])

        evidence_summaries = (
            {
                "error": "one record could not be expanded",
                "records": [{"primaryAccession": "P04637"}],
            },
            {
                "payload": {
                    "errors": [
                        {
                            "message": "ignored diagnostic identifier",
                            "primaryAccession": "Q9Y6K9",
                        }
                    ],
                    "response": {
                        "records": [{"primaryAccession": "P04637"}],
                    },
                }
            },
        )
        for summary in evidence_summaries:
            with self.subTest(summary=summary):
                output = CONTRACT.apply_source_contract(
                    {"ok": True, "status_code": 200, "summary": summary},
                    "uniprot-skill",
                    "https://rest.uniprot.org/uniprotkb/search",
                )
                self.assertTrue(output["sources"][0]["supports_claim"])
                self.assertEqual(
                    "https://www.uniprot.org/uniprotkb/P04637/entry",
                    output["sources"][0]["canonical_url"],
                )
                self.assertNotIn("checked_sources", output)

    def test_zero_count_does_not_override_records_or_coerce_other_strings(self) -> None:
        evidence_cases = (
            {
                "Count": " 0 ",
                "records": [{"primaryAccession": "P04637"}],
            },
            {
                "Count": "0",
                "payload": {"records": [{"primaryAccession": "P04637"}]},
            },
            {"Count": "0", "IdList": ["22966082"]},
            {"Count": "0", "IDs": "22966082"},
            {"Count": "unknown", "IdList": ["22966082"]},
            {"Count": True, "uids": ["22966082"]},
            {
                "pagination": {
                    "Count": "0",
                    "records": [{"primaryAccession": "P04637"}],
                }
            },
            {
                "pagination": {
                    "pages": [
                        {"records": [{"primaryAccession": "P04637"}]},
                    ]
                }
            },
        )
        for summary in evidence_cases:
            with self.subTest(summary=summary):
                output = CONTRACT.apply_source_contract(
                    {"ok": True, "summary": summary},
                    "ncbi-entrez-skill",
                    "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi",
                )
                self.assertTrue(output["sources"][0]["supports_claim"])
                self.assertNotIn("checked_sources", output)

        empty_cases = (
            {"Count": True, "IdList": []},
            {"Count": True, "IdList": True},
            {"Count": True, "IdList": [True]},
            {"Count": "unknown", "uids": []},
            {"Count": "unknown", "IDs": ""},
        )
        for summary in empty_cases:
            with self.subTest(summary=summary):
                output = CONTRACT.apply_source_contract(
                    {"ok": True, "summary": summary},
                    "ncbi-entrez-skill",
                    "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi",
                )
                self.assertNotIn("sources", output)
                self.assertEqual("empty", output["checked_sources"][0]["reason"])

        for count in (True, "unknown"):
            with self.subTest(count_only=count):
                output = CONTRACT.apply_source_contract(
                    {"ok": True, "summary": {"Count": count}},
                    "ncbi-entrez-skill",
                    "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi",
                )
                self.assertNotIn("sources", output)
                self.assertEqual("metadata", output["checked_sources"][0]["reason"])

        top_level_boolean_collection = CONTRACT.apply_source_contract(
            {"ok": True, "records": True},
            "uniprot-skill",
            "https://rest.uniprot.org/uniprotkb/search",
        )
        self.assertNotIn("sources", top_level_boolean_collection)
        self.assertEqual("empty", top_level_boolean_collection["checked_sources"][0]["reason"])

        top_level_boolean_list = CONTRACT.apply_source_contract(
            {"ok": True, "records": [True]},
            "uniprot-skill",
            "https://rest.uniprot.org/uniprotkb/search",
        )
        self.assertNotIn("sources", top_level_boolean_list)
        self.assertEqual("empty", top_level_boolean_list["checked_sources"][0]["reason"])

        top_level_cases = (
            {
                "record_count_returned": "0",
                "records": [{"primaryAccession": "P04637"}],
            },
            {
                "result_count": " 0.0e3 ",
                "results": [{"primaryAccession": "P04637"}],
            },
        )
        for payload in top_level_cases:
            with self.subTest(payload=payload):
                output = CONTRACT.apply_source_contract(
                    {"ok": True, **payload},
                    "uniprot-skill",
                    "https://rest.uniprot.org/uniprotkb/P04637",
                )
                self.assertTrue(output["sources"][0]["supports_claim"])
                self.assertNotIn("checked_sources", output)

        stale_top_level_cases = (
            {
                "record_count_returned": "0",
                "summary": {
                    "payload": {"results": [{"primaryAccession": "P04637"}]},
                },
            },
            {
                "records": [],
                "summary": {
                    "payload": {"results": [{"primaryAccession": "P04637"}]},
                },
            },
        )
        for payload in stale_top_level_cases:
            with self.subTest(stale_top_level=payload):
                output = CONTRACT.apply_source_contract(
                    {"ok": True, **payload},
                    "uniprot-skill",
                    "https://rest.uniprot.org/uniprotkb/search",
                )
                self.assertTrue(output["sources"][0]["supports_claim"])
                self.assertNotIn("checked_sources", output)

    def test_synthesis_propagates_only_deduplicated_evidence_bearing_sources(
        self,
    ) -> None:
        supported = CONTRACT.apply_source_contract(
            {"ok": True, "records": [{"primaryAccession": "P04637"}]},
            "uniprot-skill",
            "https://rest.uniprot.org/uniprotkb/P04637",
        )
        empty = CONTRACT.apply_source_contract(
            {"ok": True, "records": []}, "reactome-skill", "https://reactome.org/"
        )
        metadata = CONTRACT.apply_source_contract(
            {"ok": True, "summary": {"status": "ok"}},
            "clinicaltrials-skill",
            "https://clinicaltrials.gov/api/v2/studies/metadata",
        )
        failed = {
            "ok": False,
            "sources": [{"supports_claim": True, "kind": "evidence"}],
        }
        sources = CONTRACT.evidence_sources((supported, empty, metadata, failed, supported))
        self.assertEqual(1, len(sources))
        self.assertEqual("UniProt", sources[0]["name"])

    def test_open_targets_heatmap_preserves_target_and_disease_record_links(
        self,
    ) -> None:
        output = CONTRACT.apply_source_contract(
            {
                "ok": True,
                "summary": {"target": {"id": "ENSG00000141510"}, "returned_rows": 1},
                "matrix": {
                    "target": {"id": "ENSG00000141510"},
                    "rows": [{"disease_id": "EFO_0000311", "disease_name": "cancer"}],
                },
            },
            "opentargets-skill",
            "https://api.platform.opentargets.org/api/v4/graphql",
        )
        self.assertEqual(
            "https://platform.opentargets.org/target/ENSG00000141510",
            output["matrix"]["target"]["canonical_url"],
        )
        self.assertEqual(
            "https://platform.opentargets.org/disease/EFO_0000311",
            output["matrix"]["rows"][0]["canonical_url"],
        )
        self.assertEqual(2, len(output["sources"][0]["canonical_urls"]))

    def test_open_targets_graphql_nested_target_and_disease_ids_are_canonical(
        self,
    ) -> None:
        examples = (
            (
                {"target": {"id": "ENSG00000141510", "approvedSymbol": "TP53"}},
                "target",
                "https://platform.opentargets.org/target/ENSG00000141510",
            ),
            (
                {"disease": {"id": "EFO_0000311", "name": "asthma"}},
                "disease",
                "https://platform.opentargets.org/disease/EFO_0000311",
            ),
        )
        for summary, key, expected in examples:
            with self.subTest(key=key):
                output = CONTRACT.apply_source_contract(
                    {"ok": True, "summary": summary},
                    "opentargets-skill",
                    "https://api.platform.opentargets.org/api/v4/graphql",
                )
                self.assertEqual(expected, output["summary"][key]["canonical_url"])
                self.assertEqual(expected, output["sources"][0]["canonical_url"])

    def test_contextual_civic_and_gnomad_graphql_ids_are_not_cross_cited(self) -> None:
        civic = CONTRACT.apply_source_contract(
            {
                "ok": True,
                "summary": {
                    "variant": {"id": 12345},
                    "evidence": {"id": 67890},
                },
            },
            "civic-skill",
            "https://civicdb.org/api/graphql",
        )
        self.assertEqual(
            "https://civicdb.org/variants/12345/summary",
            civic["summary"]["variant"]["canonical_url"],
        )
        self.assertEqual(
            "https://civicdb.org/evidence/67890/summary",
            civic["summary"]["evidence"]["canonical_url"],
        )
        self.assertIsNone(CONTRACT.canonical_record_url("civic-skill", {"id": 12345}))

        gnomad = CONTRACT.apply_source_contract(
            {"ok": True, "summary": {"gene": {"id": "ENSG00000141510"}}},
            "gnomad-graphql-skill",
            "https://gnomad.broadinstitute.org/api",
        )
        self.assertEqual(
            "https://gnomad.broadinstitute.org/gene/ENSG00000141510",
            gnomad["summary"]["gene"]["canonical_url"],
        )


class SpecializedClientSafetyTests(unittest.TestCase):
    def test_graphql_upstream_error_payloads_never_expose_secrets_or_queries(
        self,
    ) -> None:
        paths = (
            SKILLS_ROOT / "civic-skill" / "scripts" / "civic_graphql.py",
            SKILLS_ROOT / "gnomad-graphql-skill" / "scripts" / "gnomad_graphql.py",
            SKILLS_ROOT / "opentargets-skill" / "scripts" / "opentargets_graphql.py",
        )
        for index, path in enumerate(paths):
            with self.subTest(skill=path.parents[1].name):
                module = _load_module(f"safe_graphql_client_{index}", path)
                response = Mock()
                response.json.return_value = {
                    "errors": [
                        {
                            "message": "api_key=TOP-SECRET query=PRIVATE-PATIENT",
                            "extensions": {"token": "BEARER-SECRET"},
                        }
                    ]
                }
                response.text = json.dumps(response.json.return_value)
                response.content = response.text.encode("utf-8")
                with patch.object(module.requests, "post", return_value=response):
                    output = module.execute({"query": "query Example { __typename }"})
                self.assertFalse(output["ok"])
                self.assertEqual("graphql_error", output["error"]["code"])
                for forbidden in ("TOP-SECRET", "PRIVATE-PATIENT", "BEARER-SECRET"):
                    self.assertNotIn(forbidden, json.dumps(output))

    def test_multipage_clinicaltrials_preserves_every_original_wire_payload(
        self,
    ) -> None:
        module = _load_module(
            "clinical_trials_raw_pages_client",
            SKILLS_ROOT / "clinicaltrials-skill" / "scripts" / "clinicaltrials_client.py",
        )
        first = b'{ "studies": [{"nctId":"NCT01234567"}], "nextPageToken":"next" }\r\n'
        second = b'{\n "studies": [{"nctId":"NCT07654321"}]\n}\n'
        responses = []
        for raw in (first, second):
            response = Mock()
            response.content = raw
            response.text = raw.decode("utf-8")
            response.json.return_value = json.loads(raw)
            responses.append(response)
        session = Mock()
        session.get.side_effect = responses
        with tempfile.TemporaryDirectory() as directory:
            requested = Path(directory) / "clinical-trials.json"
            with patch.object(module.requests, "Session", return_value=session):
                output = module.execute(
                    {
                        "action": "studies",
                        "max_pages": 2,
                        "save_raw": True,
                        "raw_output_path": str(requested),
                    }
                )
            self.assertTrue(output["ok"])
            self.assertEqual(first, requested.read_bytes())
            self.assertEqual(str(requested), output["raw_page_paths"][0])
            sidecar = Path(output["raw_page_paths"][1])
            self.assertEqual("clinical-trials.page-2.json", sidecar.name)
            self.assertEqual(second, sidecar.read_bytes())
            self.assertEqual(
                "https://clinicaltrials.gov/study/NCT01234567",
                output["records"][0]["canonical_url"],
            )


class RuntimeRawOutputTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.client = _load_module(
            "uniprot_raw_preservation_client",
            SKILLS_ROOT / "uniprot-skill" / "scripts" / "rest_request.py",
        )

    def _execute_raw(
        self,
        raw: str,
        *,
        content_type: str,
        response_format: str,
        wire_bytes: bytes | None = None,
    ) -> tuple[dict[str, Any], bytes]:
        response = Mock()
        response.text = raw
        response.content = wire_bytes if wire_bytes is not None else raw.encode("utf-8")
        response.headers = {"content-type": content_type}
        response.status_code = 200
        response.url = "https://rest.uniprot.org/uniprotkb/P04637?api_key=secret&query=private"
        if response_format == "json":
            response.json.return_value = json.loads(raw)
        session = Mock()
        session.request.return_value = response
        with tempfile.TemporaryDirectory() as directory:
            output_path = Path(directory) / "raw-response.data"
            with patch.object(self.client.requests, "Session", return_value=session):
                result = self.client.execute(
                    {
                        "base_url": "https://rest.uniprot.org",
                        "path": "uniprotkb/P04637",
                        "response_format": response_format,
                        "save_raw": True,
                        "raw_output_path": str(output_path),
                    }
                )
            return result, output_path.read_bytes()

    def test_requested_raw_json_is_byte_preserved(self) -> None:
        raw = '{  "primaryAccession" : "P04637",\n  "gene" : "TP53" }\n'
        result, saved = self._execute_raw(
            raw, content_type="application/json", response_format="json"
        )
        self.assertTrue(result["ok"])
        self.assertEqual(raw.encode("utf-8"), saved)
        self.assertNotIn("canonical_url", saved.decode("utf-8"))

    def test_requested_raw_xml_is_byte_preserved(self) -> None:
        raw = '<?xml version="1.0"?>\n<record accession="P04637"> TP53 </record>\n'
        result, saved = self._execute_raw(
            raw, content_type="application/xml", response_format="text"
        )
        self.assertTrue(result["ok"])
        self.assertEqual(raw.encode("utf-8"), saved)

    def test_requested_raw_fasta_is_byte_preserved(self) -> None:
        raw = ">sp|P04637|P53_HUMAN Cellular tumor antigen p53\nMEEPQSDPSV\n"
        result, saved = self._execute_raw(raw, content_type="text/plain", response_format="text")
        self.assertTrue(result["ok"])
        self.assertEqual(raw.encode("utf-8"), saved)

    def test_non_utf8_wire_bytes_are_preserved_without_reencoding(self) -> None:
        result, saved = self._execute_raw(
            "café",
            content_type="text/plain; charset=iso-8859-1",
            response_format="text",
            wire_bytes=b"caf\xe9",
        )
        self.assertTrue(result["ok"])
        self.assertEqual(b"caf\xe9", saved)

    def test_utf8_bom_wire_bytes_are_preserved(self) -> None:
        result, saved = self._execute_raw(
            "<record>TP53</record>",
            content_type="application/xml",
            response_format="text",
            wire_bytes=b"\xef\xbb\xbf<record>TP53</record>",
        )
        self.assertTrue(result["ok"])
        self.assertEqual(b"\xef\xbb\xbf<record>TP53</record>", saved)

    def test_generic_client_does_not_leak_api_keys_or_query_terms_on_failure(
        self,
    ) -> None:
        session = Mock()
        session.request.side_effect = self.client.requests.RequestException(
            "Request failed: https://example.org/?api_key=secret&query=private-patient"
        )
        with patch.object(self.client.requests, "Session", return_value=session):
            output = self.client.execute(
                {"base_url": "https://rest.uniprot.org", "path": "uniprotkb/P04637"}
            )
        self.assertFalse(output["ok"])
        self.assertNotIn("secret", json.dumps(output))
        self.assertNotIn("private-patient", json.dumps(output))


if __name__ == "__main__":
    unittest.main()
