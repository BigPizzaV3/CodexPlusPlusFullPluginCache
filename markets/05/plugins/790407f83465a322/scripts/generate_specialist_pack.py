#!/usr/bin/env python3
"""Generate safe, reviewable enterprise delivery artifacts from an app blueprint."""
import argparse, json
from blueprint_schema import load_blueprint
from synthetic_data import generate_samples
from pathlib import Path

def load(path):
    with open(path, encoding="utf-8") as f: return json.load(f)

def main():
    p=argparse.ArgumentParser(); p.add_argument("blueprint"); p.add_argument("--output", required=True); args=p.parse_args()
    bp=load_blueprint(args.blueprint); samples=generate_samples(bp); out=Path(args.output); out.mkdir(parents=True, exist_ok=False)
    tables=bp["dataModel"]["tables"]; names=[t.get("logicalName",t.get("name","unnamed")) for t in tables]
    fields=[(n,c["logicalName"],c.get("type","unknown")) for n,t in zip(names,tables) for c in t.get("columns",[])]
    sensitive=[x for x in fields if x[2].lower() in {"email","phone","url","multiline text","file","image"}]
    def write(name,text): (out/name).write_text(text, encoding="utf-8")
    write("dependency-risk.md", "# Dependency & Merge Resolver\n\n## Components\n"+"\n".join(f"- `{n}`" for n in names)+"\n\n## Merge gates\n- Export both unmanaged solutions and compare component IDs before import.\n- Block delete/rename changes without a migration and rollback plan.\n- Resolve shared form, view, sitemap and relationship edits in the source branch; never hand-merge solution XML.\n")
    write("migration-runbook.md", "# Data Migration & Cutover Runbook\n\n1. Freeze source writes or record a watermark.\n2. Map each source field to a Dataverse column and validate alternate keys.\n3. Dry-run with a non-production sample; reconcile count, nulls and references.\n4. Execute in batches with idempotent upsert keys.\n5. Validate counts, exceptions and security visibility before go-live.\n6. Roll back by disabling the app/flow and restoring from the approved backup strategy.\n\nNo data is migrated by this artifact.\n")
    write("synthetic-test-data.json", json.dumps({"classification":"synthetic-no-production-pii","tables":samples}, indent=2))
    write("mobile-offline-readiness.md", "# Mobile & Offline Readiness\n\n- [ ] Define offline profile tables, relationships and sync filters.\n- [ ] Test conflict behaviour, intermittent network and device form factors.\n- [ ] Keep forms compact; verify commands and embedded controls on mobile.\n- [ ] Do not assume file/image/real-time integration support offline.\n")
    write("localization-matrix.csv", "table,column,de-DE,en-US,status\n"+"\n".join(f"{t},{f},TODO,TODO,translation-required" for t,f,_ in fields)+"\n")
    write("integration-contract.md", "# Integration Contract Test\n\nRequired contract fields: endpoint owner, authentication method, schema version, idempotency key, timeout, retry/backoff, rate limit, error mapping, monitoring and data classification.\n\nContract tests are blocked until a concrete API contract is supplied.\n")
    write("threat-model.md", "# Security Threat Model\n\n## Assets\n"+"\n".join(f"- {t}" for t in names)+"\n\n## Required controls\n- Least-privilege security roles and field security for sensitive data.\n- Managed identity/service principal where applicable; never place secrets in app assets.\n- Server-side validation, audit evidence, approved solution deployment and incident owner.\n\n## Sensitive field candidates\n"+"\n".join(f"- {t}.{f} ({k})" for t,f,k in sensitive or [("none","none","none")])+"\n")
    write("copilot-guardrails.md", "# Copilot Evaluation & Red Teaming\n\n- [ ] Approved use case, data boundary and human escalation path.\n- [ ] Prompt-injection, data-exfiltration and unsafe-action test cases.\n- [ ] Grounding sources, retention, audit and kill-switch defined.\n- [ ] No autonomous write action without explicit approved execution manifest.\n")
    write("scale-resilience.md", "# Scale & Resilience Assessment\n\n- Baseline query volume, record growth, API limits and latency SLOs before production.\n- Use indexed/filterable fields, pagination, asynchronous integrations and retry with idempotency.\n- Load-test realistic queries in a non-production environment; document degradation and recovery.\n")
    write("maker-enablement.md", "# Maker Enablement Pack\n\n## Start here\n1. Work only in an unmanaged development solution.\n2. Use the Blueprint, Quality Gates and Change Capsule before deployment.\n3. Add changes through maker tools; export and validate evidence.\n\n## Roles\nMaker designs; reviewer approves; release owner imports; admin owns environment policy.\n")
    write("release-war-room.md", "# Release War Room\n\n## Go/No-go\n- Approved change capsule and target environment confirmed\n- Backup/rollback owner, release owner and incident channel named\n- Solution import, smoke test, telemetry and business validation planned\n\n## During/after\nRecord timestamps and evidence; stop on failed smoke test; roll back through the approved release path.\n")
    print(f"Created specialist delivery pack at {out}")
if __name__ == "__main__": main()
