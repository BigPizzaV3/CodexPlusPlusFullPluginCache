from __future__ import annotations

import json
import sqlite3
from dataclasses import asdict, dataclass, field
from typing import Any, Callable, Iterable

from . import audit as independent_audit
from .jsonutil import canonical_json, normalize_json_text, sha256_json, sha256_text
from .kernel import (
    Mutation,
    TurnDraft,
    commit_turn,
    current_runtime_hash,
    stable_source_turn_id,
)
from .verify import verify_database


class CompilerError(RuntimeError):
    pass


class SemanticAuditBlocked(CompilerError):
    def __init__(self, findings: Iterable[str]):
        self.findings = tuple(findings)
        super().__init__("semantic audit blocked output: " + ", ".join(self.findings))


class CompilerGameplayDisabled(CompilerError):
    pass


REQUIRED_DOMAINS = tuple(sorted(independent_audit.REQUIRED_RETRIEVAL_DOMAINS))


@dataclass(frozen=True)
class TurnRequest:
    campaign_id: str
    conversation_id: str
    message_id: str
    exact_player_message: str
    request_class: str
    phase_id: str
    expected_runtime_hash: str
    source_message_id: str | None = None
    gameplay_authorized: bool = False
    synthetic: bool = False
    presentation_mode: str = "STANDARD"


@dataclass(frozen=True)
class RetrievalBundle:
    domains: dict[str, list[str]]
    visible_refs: tuple[str, ...]
    sealed_refs: tuple[str, ...]
    sealed_terms: tuple[str, ...]
    book_preflight: dict[str, Any]


@dataclass(frozen=True)
class TurnCandidate:
    phase_before: str
    step_before: str
    phase_after: str
    step_after: str
    adjudication: dict[str, Any]
    narration: str
    visible_deltas: tuple[dict[str, Any], ...]
    sealed_deltas: tuple[dict[str, Any], ...]
    semantics: dict[str, Any]
    mutations: tuple[Mutation, ...]
    elapsed_min_seconds: int
    elapsed_max_seconds: int


@dataclass(frozen=True)
class CompileResult:
    result_id: str
    intent_id: str
    candidate_id: str
    audit_id: str
    transaction_id: str
    narration: str
    visible_deltas: tuple[dict[str, Any], ...]
    attempts: int
    post_commit: dict[str, Any]


CandidateFactory = Callable[[int, tuple[str, ...]], TurnCandidate]


def _persist_intent_and_retrieval(
    connection: sqlite3.Connection,
    request: TurnRequest,
    retrieval: RetrievalBundle,
) -> tuple[str, str]:
    if request.request_class not in {"CONTROL", "GAMEPLAY"}:
        raise CompilerError(f"unsupported request class: {request.request_class}")
    if request.presentation_mode not in {"CINEMATIC", "STANDARD", "FORENSIC"}:
        raise CompilerError(f"unsupported presentation mode: {request.presentation_mode}")
    if not request.synthetic and not request.gameplay_authorized:
        raise CompilerGameplayDisabled("gameplay compilation requires explicit authorization")
    source_turn_id = stable_source_turn_id(
        request.campaign_id, request.conversation_id, request.message_id
    )
    intent_id = f"intent:{sha256_text(source_turn_id)[:32]}"
    retrieved = sorted(
        domain for domain, refs in retrieval.domains.items() if refs is not None
    )
    complete = set(retrieved) == set(REQUIRED_DOMAINS)
    receipt_material = {
        "intent_id": intent_id,
        "required_domains": REQUIRED_DOMAINS,
        "retrieved_domains": retrieved,
        "visible_refs": sorted(retrieval.visible_refs),
        "sealed_refs_hash": sha256_json(sorted(retrieval.sealed_refs)),
        "book_preflight": retrieval.book_preflight,
        "complete": complete,
    }
    receipt_id = f"retrieval:{sha256_json(receipt_material)[:32]}"
    with connection:
        connection.execute(
            """
            INSERT INTO turn_intent(
                intent_id,campaign_id,source_turn_id,source_message_id,
                exact_player_message,exact_player_message_sha256,request_class,
                phase_id,expected_runtime_hash,gameplay_authorized,synthetic
            ) VALUES(?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                intent_id,
                request.campaign_id,
                source_turn_id,
                request.source_message_id,
                request.exact_player_message,
                sha256_text(request.exact_player_message),
                request.request_class,
                request.phase_id,
                request.expected_runtime_hash,
                int(request.gameplay_authorized),
                int(request.synthetic),
            ),
        )
        connection.execute(
            """
            INSERT INTO retrieval_receipt(
                retrieval_receipt_id,intent_id,required_domains_json,
                retrieved_domains_json,visible_refs_json,sealed_refs_hash,
                campaign_book_preflight_json,complete,content_sha256
            ) VALUES(?,?,?,?,?,?,?,?,?)
            """,
            (
                receipt_id,
                intent_id,
                canonical_json(REQUIRED_DOMAINS),
                canonical_json(retrieved),
                canonical_json(sorted(retrieval.visible_refs)),
                sha256_json(sorted(retrieval.sealed_refs)),
                canonical_json(retrieval.book_preflight),
                int(complete),
                sha256_json(receipt_material),
            ),
        )
    return intent_id, receipt_id


def _audit_envelope(
    request: TurnRequest,
    retrieval: RetrievalBundle,
    candidate: TurnCandidate,
) -> dict[str, Any]:
    semantics = dict(candidate.semantics)
    semantics["retrieval_domains"] = sorted(
        domain for domain, refs in retrieval.domains.items() if refs is not None
    )
    semantics["book_preflight"] = retrieval.book_preflight
    semantics.setdefault("sealed_refs", list(retrieval.sealed_refs))
    return {
        "schema": "aidm4.semantic_audit_envelope.v1",
        "source": {
            "exact_player_message": request.exact_player_message,
            "exact_player_message_sha256": sha256_text(request.exact_player_message),
            "sealed_terms": list(retrieval.sealed_terms),
        },
        "phase": {
            "before": [candidate.phase_before, candidate.step_before],
            "after": [candidate.phase_after, candidate.step_after],
        },
        "adjudication": candidate.adjudication,
        "output": {
            "narration": candidate.narration,
            "visible_deltas": list(candidate.visible_deltas),
        },
        "semantics": semantics,
    }


def _persist_candidate_and_audit(
    connection: sqlite3.Connection,
    intent_id: str,
    retrieval_receipt_id: str,
    attempt: int,
    candidate: TurnCandidate,
    envelope: dict[str, Any],
    result: independent_audit.AuditResult,
) -> tuple[str, str]:
    candidate_material = {
        "intent_id": intent_id,
        "retrieval_receipt_id": retrieval_receipt_id,
        "attempt": attempt,
        "phase_before": candidate.phase_before,
        "step_before": candidate.step_before,
        "phase_after": candidate.phase_after,
        "step_after": candidate.step_after,
        "adjudication": candidate.adjudication,
        "visible_deltas": candidate.visible_deltas,
        "sealed_deltas": candidate.sealed_deltas,
        "narration": candidate.narration,
        "semantic_envelope": envelope,
        "disposition": "ACCEPTED" if result.passed else "REJECTED",
    }
    candidate_id = f"candidate:{sha256_json(candidate_material)[:32]}"
    audit_id = f"audit:{result.result_sha256[:32]}"
    with connection:
        connection.execute(
            """
            INSERT INTO compiler_candidate(
                candidate_id,intent_id,retrieval_receipt_id,attempt,
                phase_before,step_before,phase_after,step_after,
                adjudication_json,visible_deltas_json,sealed_deltas_json,
                narration_draft,narration_sha256,semantic_envelope_json,
                disposition,content_sha256
            ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                candidate_id,
                intent_id,
                retrieval_receipt_id,
                attempt,
                candidate.phase_before,
                candidate.step_before,
                candidate.phase_after,
                candidate.step_after,
                canonical_json(candidate.adjudication),
                canonical_json(candidate.visible_deltas),
                canonical_json(candidate.sealed_deltas),
                candidate.narration,
                sha256_text(candidate.narration),
                canonical_json(envelope),
                "ACCEPTED" if result.passed else "REJECTED",
                sha256_json(candidate_material),
            ),
        )
        connection.execute(
            """
            INSERT INTO semantic_audit_run(
                audit_id,candidate_id,auditor_id,auditor_code_sha256,
                input_sha256,passed,finding_count,result_sha256
            ) VALUES(?,?,?,?,?,?,?,?)
            """,
            (
                audit_id,
                candidate_id,
                result.auditor_id,
                result.auditor_code_sha256,
                result.input_sha256,
                int(result.passed),
                len(result.findings),
                result.result_sha256,
            ),
        )
        for ordinal, finding in enumerate(result.findings):
            finding_id = f"finding:{sha256_json({'audit': audit_id, 'ordinal': ordinal, 'code': finding.code, 'evidence': finding.evidence})[:32]}"
            connection.execute(
                """
                INSERT INTO semantic_finding(
                    finding_id,audit_id,ordinal,invariant_code,severity,message,evidence_json
                ) VALUES(?,?,?,?,?,?,?)
                """,
                (
                    finding_id,
                    audit_id,
                    ordinal,
                    finding.code,
                    finding.severity,
                    finding.message,
                    canonical_json(finding.evidence),
                ),
            )
    return candidate_id, audit_id


def compile_turn(
    connection: sqlite3.Connection,
    request: TurnRequest,
    retrieval: RetrievalBundle,
    candidate_factory: CandidateFactory,
    *,
    max_attempts: int = 3,
) -> CompileResult:
    if max_attempts < 1:
        raise CompilerError("max_attempts must be positive")
    intent_id, retrieval_receipt_id = _persist_intent_and_retrieval(
        connection, request, retrieval
    )
    prior_findings: tuple[str, ...] = ()
    for attempt in range(1, max_attempts + 1):
        candidate = candidate_factory(attempt, prior_findings)
        envelope = _audit_envelope(request, retrieval, candidate)
        audit_result = independent_audit.audit(envelope)
        candidate_id, audit_id = _persist_candidate_and_audit(
            connection,
            intent_id,
            retrieval_receipt_id,
            attempt,
            candidate,
            envelope,
            audit_result,
        )
        if not audit_result.passed:
            prior_findings = tuple(finding.code for finding in audit_result.findings)
            continue

        result_id = f"result:{sha256_json({'intent': intent_id, 'candidate': candidate_id, 'audit': audit_id})[:32]}"

        def compiler_side_effect(db: sqlite3.Connection, transaction_id: str) -> None:
            db.execute(
                """
                INSERT INTO compiler_result(
                    result_id,intent_id,candidate_id,audit_id,transaction_id,
                    visible_narration,visible_deltas_json,presentation_mode,
                    runtime_hash_after,status
                ) VALUES(?,?,?,?,?,?,?,?,?,?)
                """,
                (
                    result_id,
                    intent_id,
                    candidate_id,
                    audit_id,
                    transaction_id,
                    candidate.narration,
                    canonical_json(candidate.visible_deltas),
                    request.presentation_mode,
                    current_runtime_hash(db),
                    "COMMITTED_VALIDATED",
                ),
            )

        draft = TurnDraft(
            source_turn_id=stable_source_turn_id(
                request.campaign_id, request.conversation_id, request.message_id
            ),
            source_message_id=request.source_message_id,  # type: ignore[arg-type]
            expected_runtime_hash=request.expected_runtime_hash,
            phase_before=candidate.phase_before,
            step_before=candidate.step_before,
            phase_after=candidate.phase_after,
            step_after=candidate.step_after,
            player_declaration=request.exact_player_message,
            adjudication={
                **candidate.adjudication,
                "semantic_audit_id": audit_id,
                "compiler_candidate_id": candidate_id,
            },
            narration=candidate.narration,
            elapsed_min_seconds=candidate.elapsed_min_seconds,
            elapsed_max_seconds=candidate.elapsed_max_seconds,
            mutations=candidate.mutations,
            schema_version=2,
        )
        transaction_id = commit_turn(
            connection,
            draft,
            transaction_side_effect=compiler_side_effect,
        )
        integrity = verify_database(connection)
        output_hash = sha256_json(
            {
                "result_id": result_id,
                "narration": candidate.narration,
                "visible_deltas": candidate.visible_deltas,
            }
        )
        dependency_hash = sha256_json(
            {
                "transaction_id": transaction_id,
                "runtime_hash": current_runtime_hash(connection),
                "candidate_id": candidate_id,
            }
        )
        rebuild_id = f"rebuild:{sha256_json({'kind': 'TURN_RESULT', 'dependency': dependency_hash, 'output': output_hash})[:32]}"
        with connection:
            connection.execute(
                """
                INSERT OR IGNORE INTO projection_rebuild_receipt(
                    rebuild_id,projection_kind,source_transaction_hash,
                    dependency_hash,output_hash,row_count,deterministic
                ) VALUES(?,?,?,?,?,?,?)
                """,
                (
                    rebuild_id,
                    "TURN_RESULT",
                    connection.execute(
                        "SELECT transaction_hash FROM transaction_log WHERE transaction_id=?",
                        (transaction_id,),
                    ).fetchone()[0],
                    dependency_hash,
                    output_hash,
                    len(candidate.visible_deltas) + 1,
                    1,
                ),
            )
        return CompileResult(
            result_id=result_id,
            intent_id=intent_id,
            candidate_id=candidate_id,
            audit_id=audit_id,
            transaction_id=transaction_id,
            narration=candidate.narration,
            visible_deltas=candidate.visible_deltas,
            attempts=attempt,
            post_commit=integrity,
        )
    raise SemanticAuditBlocked(prior_findings)


@dataclass(frozen=True)
class ClaimCorrection:
    target_claim_id: str
    object_value: Any
    affected_projection: str
    predicate: str | None = None
    subject: str | None = None


def rebuild_claim_projection(
    connection: sqlite3.Connection,
    *,
    source_transaction_hash: str,
) -> dict[str, Any]:
    claims = [dict(row) for row in connection.execute("SELECT * FROM claim ORDER BY claim_id")]
    links = [
        dict(row)
        for row in connection.execute(
            "SELECT * FROM claim_link ORDER BY source_claim_id,target_claim_id,relation"
        )
    ]
    superseded = {
        link["target_claim_id"]
        for link in links
        if link["relation"] == "SUPERSEDES"
    }
    active = [claim for claim in claims if claim["claim_id"] not in superseded]
    authority_rank = {
        "PLAYER_CORRECTED": 0,
        "PRIMARY_ESTABLISHED": 1,
        "HIDDEN_GM_CANON": 2,
        "DERIVED": 3,
        "PROVISIONAL_INFERENCE": 4,
    }
    selected: dict[tuple[str | None, str], dict[str, Any]] = {}
    for claim in active:
        key = (claim["subject"], claim["predicate"])
        existing = selected.get(key)
        score = (authority_rank.get(claim["authority_class"], 50), claim["claim_id"])
        if existing is None:
            selected[key] = claim
        else:
            existing_score = (
                authority_rank.get(existing["authority_class"], 50),
                existing["claim_id"],
            )
            if score < existing_score:
                selected[key] = claim
    dependency = {"claims": claims, "links": links}
    dependency_hash = sha256_json(dependency)
    rows = []
    for (subject, predicate), claim in sorted(
        selected.items(), key=lambda item: ((item[0][0] or ""), item[0][1])
    ):
        rows.append(
            {
                "projection_key": f"claim-projection:{sha256_json([subject, predicate])[:32]}",
                "subject": subject,
                "predicate": predicate,
                "active_claim_id": claim["claim_id"],
                "object_json": claim["object_json"],
                "authority_class": claim["authority_class"],
                "source_graph_sha256": dependency_hash,
                "visibility": claim["visibility"],
            }
        )
    output_hash = sha256_json(rows)
    with connection:
        connection.execute("DELETE FROM claim_projection")
        connection.executemany(
            """
            INSERT INTO claim_projection(
                projection_key,subject,predicate,active_claim_id,object_json,
                authority_class,source_graph_sha256,visibility
            ) VALUES(:projection_key,:subject,:predicate,:active_claim_id,:object_json,
                     :authority_class,:source_graph_sha256,:visibility)
            """,
            rows,
        )
        rebuild_id = f"rebuild:{sha256_json({'kind': 'CLAIM_CURRENT', 'dependency': dependency_hash, 'output': output_hash})[:32]}"
        connection.execute(
            """
            INSERT OR IGNORE INTO projection_rebuild_receipt(
                rebuild_id,projection_kind,source_transaction_hash,
                dependency_hash,output_hash,row_count,deterministic
            ) VALUES(?,?,?,?,?,?,?)
            """,
            (
                rebuild_id,
                "CLAIM_CURRENT",
                source_transaction_hash,
                dependency_hash,
                output_hash,
                len(rows),
                1,
            ),
        )
    return {
        "dependency_hash": dependency_hash,
        "output_hash": output_hash,
        "row_count": len(rows),
    }


def apply_correction(
    connection: sqlite3.Connection,
    *,
    correction_id: str,
    campaign_id: str,
    exact_player_correction: str,
    reason: str,
    original_result_id: str | None,
    effects: tuple[ClaimCorrection, ...],
    mutations: tuple[Mutation, ...],
    expected_runtime_hash: str,
) -> dict[str, Any]:
    if not effects:
        raise CompilerError("A correction requires at least one granular claim effect")
    if not mutations:
        raise CompilerError("A correction requires at least one typed state mutation")
    original_output = ""
    if original_result_id is not None:
        row = connection.execute(
            "SELECT visible_narration FROM compiler_result WHERE result_id=?",
            (original_result_id,),
        ).fetchone()
        if row is None:
            raise CompilerError(f"unknown original result: {original_result_id}")
        original_output = row["visible_narration"]
    replacement_rows = []
    for ordinal, effect in enumerate(effects):
        target = connection.execute(
            "SELECT * FROM claim WHERE claim_id=?", (effect.target_claim_id,)
        ).fetchone()
        if target is None:
            raise CompilerError(f"unknown target claim: {effect.target_claim_id}")
        replacement_id = f"claim:correction:{sha256_json({'correction': correction_id, 'ordinal': ordinal, 'target': effect.target_claim_id, 'object': effect.object_value})[:24]}"
        replacement_rows.append((ordinal, effect, dict(target), replacement_id))
    adjudication = {
        "kind": "PLAYER_CORRECTION",
        "correction_id": correction_id,
        "reason": reason,
        "effects": [
            {
                "target_claim_id": effect.target_claim_id,
                "replacement_claim_id": replacement_id,
                "affected_projection": effect.affected_projection,
                "object": effect.object_value,
            }
            for _, effect, _, replacement_id in replacement_rows
        ],
    }

    def correction_side_effect(db: sqlite3.Connection, transaction_id: str) -> None:
        db.execute(
            """
            INSERT INTO correction_record(
                correction_id,campaign_id,exact_player_correction,
                exact_player_correction_sha256,original_result_id,
                original_output_sha256,correction_transaction_id,reason
            ) VALUES(?,?,?,?,?,?,?,?)
            """,
            (
                correction_id,
                campaign_id,
                exact_player_correction,
                sha256_text(exact_player_correction),
                original_result_id,
                sha256_text(original_output),
                transaction_id,
                reason,
            ),
        )
        for ordinal, effect, target, replacement_id in replacement_rows:
            db.execute(
                """
                INSERT INTO claim(
                    claim_id,source_message_id,domain,subject,predicate,
                    object_json,authority_class,epistemic_class,visibility,
                    valid_from_event_id,payload_json
                ) VALUES(?,?,?,?,?,?,?,?,?,?,?)
                """,
                (
                    replacement_id,
                    None,
                    target["domain"],
                    effect.subject if effect.subject is not None else target["subject"],
                    effect.predicate if effect.predicate is not None else target["predicate"],
                    canonical_json(effect.object_value),
                    "PLAYER_CORRECTED",
                    "CONFIRMED",
                    target["visibility"],
                    target["valid_from_event_id"],
                    canonical_json(
                        {
                            "correction_id": correction_id,
                            "supersedes": effect.target_claim_id,
                        }
                    ),
                ),
            )
            db.execute(
                """
                INSERT INTO claim_link(
                    source_claim_id,target_claim_id,relation,source_ruling_id
                ) VALUES(?,?,?,NULL)
                """,
                (replacement_id, effect.target_claim_id, "SUPERSEDES"),
            )
            db.execute(
                """
                INSERT INTO correction_effect(
                    correction_id,ordinal,target_claim_id,replacement_claim_id,
                    relation,affected_projection
                ) VALUES(?,?,?,?,?,?)
                """,
                (
                    correction_id,
                    ordinal,
                    effect.target_claim_id,
                    replacement_id,
                    "SUPERSEDES",
                    effect.affected_projection,
                ),
            )

    draft = TurnDraft(
        source_turn_id=f"correction-turn:{sha256_text(correction_id + exact_player_correction)}",
        source_message_id=None,  # type: ignore[arg-type]
        expected_runtime_hash=expected_runtime_hash,
        phase_before="CONTROL",
        step_before="CORRECTION_DRAFT",
        phase_after="CONTROL",
        step_after="CORRECTION_COMMITTED",
        player_declaration=exact_player_correction,
        adjudication=adjudication,
        narration="Correction receipt only; original output remains preserved.",
        elapsed_min_seconds=0,
        elapsed_max_seconds=0,
        mutations=mutations,
        schema_version=2,
    )
    transaction_id = commit_turn(
        connection,
        draft,
        transaction_side_effect=correction_side_effect,
    )
    transaction_hash = connection.execute(
        "SELECT transaction_hash FROM transaction_log WHERE transaction_id=?",
        (transaction_id,),
    ).fetchone()[0]
    first = rebuild_claim_projection(
        connection, source_transaction_hash=transaction_hash
    )
    second = rebuild_claim_projection(
        connection, source_transaction_hash=transaction_hash
    )
    if first != second:
        raise CompilerError("claim projection rebuild is not deterministic")
    integrity = verify_database(connection)
    return {
        "schema": "aidm4.correction_receipt.v1",
        "correction_id": correction_id,
        "transaction_id": transaction_id,
        "original_result_preserved": original_result_id is not None,
        "effects": len(effects),
        "projection": first,
        "integrity": integrity["status"],
    }
