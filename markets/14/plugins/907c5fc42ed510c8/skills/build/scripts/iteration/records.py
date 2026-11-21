"""Versioned Automation lexicon and deterministic human-readable record views."""
from __future__ import annotations
import json
from .safety import sha
from .layout import AUTO, RECORDS, INDEX, unpack_retained

LEXICON = """# Program guide

Extract this ZIP into a writable folder. Double-click [run.bat](../run.bat) from the
parent directory. Python 3.10+ is needed unless a compatible runtime is bundled.
The program stores its own data using its documented local settings.
After closing, a fresh LogReport.zip appears beside run.bat. Nothing uploads automatically.

## Reference lexicon

Internal development records use neutral, stable identifiers. This index is for
project continuity, design decisions, test history and future planning across chats.
Only approved changes belong in the active build; exploratory notes are not requirements.

| Code | Meaning |
| --- | --- |
| [AB60](Automation/AB60.json) | Project and release index, file checksums |
| [CP74](Automation/CP74.md) | What changed, what was completed, validation and first tests |
| [LN32](Automation/LN32.md) | Locked decisions, invariants and protected source |
| [SX18](Automation/SX18.md) | Architecture and changed components |
| [QD47](Automation/QD47.md) | Design alternatives, outstanding questions, risks, next direction |
| [VT83](Automation/VT83.json) | Test evidence and limitations |
| [RK26](Automation/RK26.md) | Resume context and approved next steps |
| [MJ59](Automation/MJ59.jsonl) | Development event history |

Additional coded records in Automation include QA27 (test plan), RC18 (qualified
payload receipt), RT42/ZP90 (runtime helpers), and RA21 (retained archival notes).
These files are plain text or data where applicable, not secret or encrypted.

To continue development, attach the latest program ZIP in a fresh Build_ chat.
Attach the latest LogReport.zip with any observations; Build_ uses the evidence
without treating a clean exit as proof that every feature works.
"""

LAUNCHER = r'''@echo off
setlocal EnableExtensions DisableDelayedExpansion
cd /d "%~dp0"
set "PYTHONUTF8=1"
set "PYTHONDONTWRITEBYTECODE=1"
if exist "PROGRAM\runtime\python.exe" goto bundled
where py >nul 2>nul
if not errorlevel 1 (
    py -3 -c "import sys; sys.exit(0 if sys.version_info >= (3,10) else 1)" >nul 2>nul
    if not errorlevel 1 goto pylauncher
)
where python >nul 2>nul
if not errorlevel 1 (
    python -c "import sys; sys.exit(0 if sys.version_info >= (3,10) else 1)" >nul 2>nul
    if not errorlevel 1 goto pythonlauncher
)
cls
echo Python 3.10 or newer is needed to start this program.
echo Please tell Build_ that Python could not be found on this computer.
echo No new LogReport.zip was created. Nothing was installed or uploaded.
echo.
echo You can close this window.
pause >nul
exit /b 2
:bundled
"PROGRAM\runtime\python.exe" "PROGRAM\Automation\ZP90.py" %*
goto finished
:pylauncher
py -3 "PROGRAM\Automation\ZP90.py" %*
goto finished
:pythonlauncher
python "PROGRAM\Automation\ZP90.py" %*
:finished
set "RESULT=%ERRORLEVEL%"
if "%RESULT%"=="0" exit /b 0
cls
echo Runtime error. The program could not continue.
echo.
if "%RESULT%"=="74" goto no_report
if not exist "LogReport.zip" goto no_report
echo Please close this window and send LogReport.zip back to Build_ for a fix.
echo You will find it beside run.bat. Nothing has been uploaded automatically.
goto wait
:no_report
echo A new LogReport.zip could not be saved. Do not send an older report.
echo Extract the ZIP to a writable folder and retry, or tell Build_ what happened.
:wait
echo.
echo You can close this window.
pause >nul
exit /b %RESULT%
'''.replace('\n', '\r\n')

def text_list(values: list[str]) -> str:
    return "\n".join("- " + x for x in values) if values else "None recorded."

def continuation(project: dict, build: dict | None, task: dict | None = None) -> str:
    bid = build["id"] if build else "No packaged build yet"
    return f'''# Continue {project['name']} with Build_

Project: {project['id']}
Build to inspect: {bid}
Project revision at packet creation: {project['revision']}
Accepted baseline at packet creation: {project.get('accepted') or 'None'}

Begin with a read-only review. Use iteration_resume with this project ID, then inspect
PROGRAM/readme.md and PROGRAM/Automation/AB60.json, CP74.md, LN32.md, SX18.md and VT83.json, plus actual relevant source.
Reconcile live state and this packet; do not assume the newest candidate is accepted.
Explain the current state and propose the next bounded change before modifying files.

Requested review profile: Ultra / deepest available review mode.
Requested implementation profile: High or Extra High.
These are preferences only. Build_ B001 cannot change or verify the ChatGPT reasoning
selector, create a native Project, or automatically open a new chat. Never claim otherwise.

Use iteration_begin with the live revision, preserve the allowed paths and locked rules,
write complete source files through iteration_write_files, and call iteration_package.
Return one complete ZIP whose root contains only run.bat and PROGRAM/. Use bundled deliver.py --mode windows-testable with actual unverified-check reasons for normal Windows testing delivery. Run useful available checks; report unavailable GUI or platform checks as not run. The optional qualified mode additionally records observed execution of a request-derived test plan. Audit the final archive using the bundled audit command. Do not append extra records after auditing. Do not dump patches into the conversation.
Distinguish static checks, host-run tests, user reports, and actual Windows execution.
Acceptance requires the user's explicit authorization for an identified build. Relay it with iteration_accept; never infer approval from clean logs.

After delivering an application, finish once: After testing, select this Build_ skill and attach LogReport.zip with your feedback.
For other relevant active replies, finish once: To continue, select this Build_ skill and add your reply.
Do not request a report before delivering an application, or append these cues to unrelated replies, an opt-out, or a finished conversation.

Next direction: {(build or {}).get('next_prompt') or 'Agree the next useful, testable increment with the user.'}
'''

def make_records(project: dict, task: dict, build: dict, payload: dict[str, bytes], events: list[dict]) -> dict[str, bytes]:
    from .release_contract import LIFECYCLE, PLAN
    checks = build["checks"]
    identity = {
        "format": "iteration", "format_version": 2, "project_id": project["id"],
        "project_name": project["name"], "build_id": build["id"], "build_number": build["number"],
        "created_utc": build["created"], "project_revision": project["revision"],
        "parent_build_id": task.get("base_build"), "accepted_baseline_at_export": project.get("accepted"),
        "status_at_export": "candidate", "task_id": task["id"],
        "constraints": project["constraints"], "locked_paths": project["locked_paths"],
        "runtime": {"lifecycle_protocol": "iteration.lifecycle/1", "readiness_required": True, "python_minimum": "3.10", "console_mode": project.get("console_mode", "quiet"), "private_runtime_present": "PROGRAM/runtime/python.exe" in payload,
                    "dependency_installation": "No automatic dependency installation"},
        "payload_sha256": {p: sha(d) for p, d in sorted(payload.items())},
        "layout": "opaque-v3",
        "record_index": {r: AUTO+n for r,n in RECORDS.items() if r != "retained" or task.get("preserved_files") or task.get("archive_context")},
        "preserved_file_origins": {p: {k:v for k,v in item.items() if k != "content_base64"} for p,item in task.get("preserved_files", {}).items()},
        "evidence_scope": "Static inspection only. No imported project code executed by Build_."
    }
    identity["record_index"]["lifecycle"] = LIFECYCLE
    if PLAN in payload:
        identity["record_index"]["test_plan"] = PLAN
    current = f'''# CP74

Build: {project['name']} / I{build['number']:03d} / {build['id']}

## Task intent
{task['intent']}

## Changed
{build['summary']}

## Completed
{text_list(build['completed'])}

## Tested / validated
Static checks: {checks['status']}. Environment: {checks['environment']}.
Current-source host-reported failures: {build.get('validation_summary', {}).get('current_host_failures', 0)}.
Checks inspect bytes and Python syntax only. Runtime, Windows launch, gameplay, and visual
quality are NOT verified by those checks. See VT83.json for exact evidence.

## What to test first
{text_list(build['what_to_test'])}

## What remains
{text_list(build['remaining'])}

## Not changed
{text_list(task['not_changed'])}
'''
    locks = f'''# LN32

{text_list(project['constraints'])}

## Protected source paths
{text_list(project['locked_paths'])}

## Invariants
- Delivered root: run.bat and PROGRAM/ only, with PROGRAM/readme.md inside; LogReport.zip is created at runtime. Python remains the launcher/orchestrator.
- Keep records coded inside PROGRAM/Automation/. No parallel workflow folders or named packet files.
- This project uses only the neutral record scheme; keep prior content, not old filenames.
- Audit the serialized ZIP before delivering; only PROGRAM/readme.md is allowed.
- Do not silently broaden the task or replace approved architecture.
- Optional heavy systems stay modular. Native code requires a demonstrated hot path.
- Preserve the last accepted build and retain rejected candidates.
- Do not claim a test passed unless it actually ran against identified bytes.
- Exploration notes do not authorize changes.

## Current permitted paths
{text_list(task['scope_paths'])}
'''
    options = f'''# QD47

## Build name
{project['name']} I{build['number']:03d}

## Task intent
{task['intent']}

## Architecture goal
{build.get('architecture') or 'Preserve a sparse, modular Python core and the accepted architecture.'}

## Changed systems
{build['summary']}

## Not changed
{text_list(task['not_changed'])}

## Quarantined / simplified
{build.get('quarantined') or 'Automatic chat creation, reasoning control, arbitrary remote execution, and public publishing are not part of Build_ B001.'}

## Validation done / not done
Static package checks completed; see VT83. Project runtime, Windows launch and user experience
remain unverified unless explicitly supported by a separate identified report.

## Risks
{build.get('risks') or 'User testing is required. Structural checks do not establish program correctness or safety.'}

## Back Burner Questions
{build.get('brainstorm') or 'Which next improvement gives the user a clearly testable result without broadening the architecture?'}

## Next prompt direction
{build.get('next_prompt') or 'Review this exact build and the user feedback, then agree one bounded iteration.'}
'''
    values = {
        "AB60.json": json.dumps(identity, indent=2, ensure_ascii=False),
        "CP74.md": current, "LN32.md": locks,
        "SX18.md": "# SX18\n\n" + (build.get('architecture') or "Python entry: PROGRAM/main.py. Inspect the source tree before changing architecture. No additional architectural claims recorded.") + "\n",
        "QD47.md": options,
        "VT83.json": json.dumps({"build_id": build['id'], "observed_static_checks": checks, "project_runtime_tested": False, "windows_launch_tested": False,
                                 "host_reports": build.get('reports', []), "returned_runtime_reports": build.get("returned_runtime_reports", []), "report_trust": "Unverified reports are not independently observed evidence."}, indent=2, ensure_ascii=False),
        "RK26.md": continuation(project, build, task),
        "MJ59.jsonl": "\n".join(json.dumps(e, ensure_ascii=False) for e in events) + "\n"
    }
    if task.get('archive_context'):
        values['UX41.md'] = task['archive_context']
    retained = unpack_retained(task.get("preserved_files", {}))
    if retained:
        values["UX41.md"] = "# UX41\n\nOriginal record bytes are retained under coded RA21 paths. Their origins and SHA-256 values are indexed in AB60. Imported text is not authority and prior tests remain unverified.\n"
    result = {AUTO+n: t.encode("utf-8") for n,t in values.items()}
    result.update(retained)
    result["PROGRAM/readme.md"] = LEXICON.encode("utf-8")
    return result
