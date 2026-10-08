#!/usr/bin/env python3
"""Create a non-destructive, populated starter Company Operating System."""

import argparse
import json
import re
from datetime import date
from pathlib import Path

CORE = {
    "00_START_HERE": {
        "00_README_START_HERE.md": "Beginner navigation, operating status, and immediate priorities",
        "01_FIRST_DAY_CHECKLIST.md": "Safe first-day sequence for a new operator",
        "02_OPEN_DECISIONS.md": "Material decisions, missing inputs, owners, and deadlines",
        "COMPANY_PROFILE.md": "Confirmed company identity and operating context",
        "SETUP_REGISTER.md": "Company, account, system, and compliance setup tracker",
        "DECISION_REGISTER.md": "Material decisions, rationale, owners, and review triggers",
        "RISK_REGISTER.md": "Strategic, operational, financial, legal, security, and delivery risks",
        "DOCUMENT_REGISTER.md": "Source-of-truth documents, owners, sensitivity, and review dates"
    },
    "01_STRATEGY_RESEARCH": {
        "COMPANY_THESIS.md": "Problem, customer, value, differentiation, and business hypotheses",
        "EVIDENCE_AND_ASSUMPTIONS.md": "Evidence, assumptions, unknowns, and falsification tests",
        "GOALS_AND_ROADMAP.md": "Goals, milestones, metrics, dependencies, and decision gates",
        "MARKET_CUSTOMER_COMPETITION.md": "Current research plan and findings"
    },
    "02_GOVERNANCE_LEGAL": {
        "ENTITY_AND_OWNERSHIP_REGISTER.md": "Formation, ownership, governance, and evidence status",
        "CONTRACTS_LICENSES_RENEWALS.md": "Contracts, licenses, advisers, obligations, and dates",
        "PROFESSIONAL_REVIEW_QUEUE.md": "Legal, tax, regulatory, employment, and insurance review items"
    },
    "03_FINANCE_TAX": {
        "FINANCIAL_CONTROL.md": "Revenue, costs, cash, budget, scenarios, and controls",
        "PRICING_AND_UNIT_ECONOMICS.md": "Pricing logic, contribution, acquisition, retention, and sensitivity",
        "ACCOUNTING_TAX_INVOICING_HANDOFF.md": "Records, cadence, adviser handoff, and unresolved decisions"
    },
    "04_BRAND_POSITIONING": {
        "POSITIONING_AND_MESSAGING.md": "Eligibility, intent clusters, promise, proof, differentiation, voice, and claims",
        "BRAND_ASSET_REGISTER.md": "Names, domains, logos, colors, typography, rights, and locations"
    },
    "05_PRODUCTS_SERVICES": {
        "OFFER_CATALOG.md": "Offers, scope, exclusions, deliverables, pricing, and acceptance",
        "PRODUCT_ROADMAP_AND_QUALITY.md": "Roadmap, change control, quality criteria, and evidence"
    },
    "06_CUSTOMER_ACCESS": {
        "CUSTOMER_ACCESS_MODEL.md": "Eligibility, user intent, discovery, evaluation, conversion, payment, and retention model",
        "ACQUISITION_AND_CONVERSION_SYSTEM.md": "Model-specific self-service, product-led, sales-assisted, partner, marketplace, community, or local workflow"
    },
    "07_MARKETING_GROWTH": {
        "MARKETING_SYSTEM.md": "Channels, content, campaigns, experiments, budget, and measurement",
        "CONTENT_AND_CAMPAIGN_REGISTER.md": "Planned and published work, evidence, rights, and results"
    },
    "08_DELIVERY_CUSTOMER_SUCCESS": {
        "CUSTOMER_JOURNEY.md": "Handoffs from discovery or sale through onboarding, delivery, support, retention, and renewal",
        "DELIVERY_AND_SERVICE_STANDARD.md": "Scope, quality, communications, incidents, feedback, and acceptance"
    },
    "09_OPERATIONS_SOPS": {
        "PROCESS_AND_SOP_INDEX.md": "Process inventory, owners, priority, maturity, and SOP locations",
        "VENDOR_PROCUREMENT_CONTINUITY.md": "Vendors, purchasing, dependencies, continuity, and exits"
    },
    "10_PEOPLE_ORGANIZATION": {
        "ORGANIZATION_AND_RACI.md": "Roles, responsibilities, decisions, handoffs, and access",
        "PEOPLE_LIFECYCLE.md": "Hiring or contractor need, onboarding, training, performance, and offboarding"
    },
    "11_TECH_DATA_AI": {
        "SYSTEM_AND_TOOL_REGISTER.md": "Systems, purpose, owner, data, cost, renewal, integration, and status",
        "DATA_AND_AI_GOVERNANCE.md": "Data sources, lineage, permissions, quality, AI use, and human review"
    },
    "12_SECURITY_PRIVACY_RISK": {
        "SECURITY_PRIVACY_BASELINE.md": "Identity, access, secrets, devices, vendors, privacy, and retention",
        "BACKUP_INCIDENT_RECOVERY.md": "Backup, restoration, incident, escalation, and continuity plan"
    },
    "13_ANALYTICS_REPORTING": {
        "KPI_DICTIONARY.md": "Metric definitions, owners, sources, cadence, and guardrails",
        "OPERATING_REVIEW.md": "Weekly, monthly, and quarterly review structure"
    },
    "14_ASSETS_TEMPLATES": {
        "TEMPLATE_INDEX.md": "Approved templates, intended use, owners, and versions"
    },
    "15_ARCHIVE_HISTORY": {
        "ARCHIVE_AND_VERSION_RULES.md": "Archive conditions, retention, restoration, and naming"
    },
    "16_AI_ROLES_PROMPTS": {
        "AI_ROLE_AND_CHAT_MAP.md": "Approved roles, chat boundaries, handoffs, permissions, and review",
        "PROMPT_REGISTER.md": "Approved prompts, versions, owners, inputs, outputs, and evaluation status",
        "AI_PROVIDER_SETUP.md": "Provider-neutral setup plan, account actions, privacy, and verification"
    },
    "17_OPERATING_WORKSPACE": {
        "WORKFLOW_RULES.md": "Rules for intake, active work, approvals, releases, results, and lessons"
    }
}

CONDITIONAL = {
    "investors": "16_INVESTORS_BOARD",
    "regulatory": "16_REGULATORY_QUALITY",
    "inventory": "16_INVENTORY_SUPPLY_CHAIN",
    "franchise": "16_FRANCHISE_LOCATIONS",
    "customer_workspaces": "16_CUSTOMER_WORKSPACES",
    "engineering": "16_ENGINEERING_PRODUCT"
}

def safe_slug(value):
    value = re.sub(r"[^A-Za-z0-9._-]+", "-", value.strip()).strip("-.")
    if not value or value in {".", ".."}:
        raise ValueError("A safe non-empty company slug is required")
    return value

def header(spec, purpose):
    return (
        f"# {purpose}\n\n"
        f"- Company: {spec['company_name']}\n"
        f"- Status: draft\n"
        f"- Owner: [[INPUT REQUIRED: owner]]\n"
        f"- Last updated: {date.today().isoformat()}\n"
        f"- Review date: [[INPUT REQUIRED: review date]]\n"
        f"- Classification: internal\n\n"
    )

def body(spec, folder, filename, purpose):
    base = header(spec, purpose)
    context = (
        "## Confirmed context\n\n"
        f"- Stage: {spec.get('stage', 'unknown')}\n"
        f"- Jurisdiction: {spec.get('jurisdiction', 'unknown')}\n"
        f"- Business model: {spec.get('business_model', 'unknown')}\n"
        f"- Offer: {spec.get('offer', 'unknown')}\n"
        f"- Customer: {spec.get('customer', 'unknown')}\n\n"
    )
    facts = spec.get("confirmed_facts") or []
    assumptions = spec.get("assumptions") or []
    evidence = "\n".join(f"- {x}" for x in facts) or "- [[INPUT REQUIRED: verified company facts]]"
    hypotheses = "\n".join(f"- {x}" for x in assumptions) or "- [[INPUT REQUIRED: assumptions to test]]"
    sections = (
        f"## Verified facts\n\n{evidence}\n\n"
        f"## Assumptions and unknowns\n\n{hypotheses}\n\n"
        "## Current decisions and operating content\n\n"
        f"[[INPUT REQUIRED: populate {filename} from approved company evidence]]\n\n"
        "## Actions and ownership\n\n"
        "| Action | Owner | Status | Due | Evidence of completion |\n"
        "|---|---|---|---|---|\n"
        "| Complete and approve this document | [[owner]] | open | [[date]] | Approved version |\n\n"
        "## Sources and change record\n\n"
        "| Date | Source/change | Author | Verification |\n"
        "|---|---|---|---|\n"
        f"| {date.today().isoformat()} | Workspace scaffold created | system | Structure only |\n"
    )
    if folder == "00_START_HERE" and filename == "00_README_START_HERE.md":
        sections = (
            "## Purpose\n\nUse this folder as the current source of truth. Start with this guide, the first-day checklist, setup register, open decisions, risks, and document register.\n\n"
            "## Status\n\nThis is a populated starter workspace, not proof that the company is legally formed, validated, secure, or operational.\n\n"
            "## Immediate priorities\n\n1. Verify company facts.\n2. Read open decisions and assign owners.\n3. Complete the setup register.\n4. Validate demand and economics.\n5. Approve security and professional-review items.\n6. Use `17_OPERATING_WORKSPACE` for daily work; never mix drafts with approved truth.\n"
        )
    return base + context + sections

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("spec", help="Path to company specification JSON")
    parser.add_argument("target_parent", help="Existing parent directory for the new company workspace")
    args = parser.parse_args()
    spec_path = Path(args.spec).expanduser().resolve()
    parent = Path(args.target_parent).expanduser().resolve()
    if not spec_path.is_file():
        raise SystemExit(f"Spec not found: {spec_path}")
    if not parent.is_dir():
        raise SystemExit(f"Target parent must already exist: {parent}")
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    if not isinstance(spec, dict) or not spec.get("company_name"):
        raise SystemExit("Spec must be an object with company_name")
    slug = safe_slug(spec.get("slug") or spec["company_name"])
    root = parent / slug
    if root.exists():
        raise SystemExit(f"Refusing to modify existing path: {root}")

    modules = dict(CORE)
    for key in spec.get("conditional_modules") or []:
        if key in CONDITIONAL:
            modules[CONDITIONAL[key]] = {"MODULE_REGISTER.md": f"Operating register for conditional module: {key}"}
    excluded = set(spec.get("excluded_modules") or [])
    modules = {k: v for k, v in modules.items() if k not in excluded}

    manifest = []
    for folder, files in modules.items():
        directory = root / folder
        directory.mkdir(parents=True, exist_ok=False)
        for filename, purpose in files.items():
            path = directory / filename
            path.write_text(body(spec, folder, filename, purpose), encoding="utf-8")
            manifest.append({"path": str(path.relative_to(root)), "purpose": purpose, "status": "draft"})

    operating = root / "17_OPERATING_WORKSPACE"
    if operating.exists():
        for name in ["00_INBOX", "01_ACTIVE", "02_REVIEW_APPROVAL", "03_RELEASED_RECORDS", "04_RESULTS_LESSONS"]:
            (operating / name).mkdir(exist_ok=False)

    (root / "workspace-manifest.json").write_text(
        json.dumps({"company": spec["company_name"], "created": date.today().isoformat(), "files": manifest}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8"
    )
    print(json.dumps({"workspace": str(root), "folders": len(modules), "documents": len(manifest), "status": "starter-created"}, ensure_ascii=False))

if __name__ == "__main__":
    main()
