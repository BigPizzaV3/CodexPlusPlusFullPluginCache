"""Small test-only protocol fixtures, never the template for a customer program."""
from __future__ import annotations
import io
import json
import zipfile
from iteration.layout import INDEX
from iteration.safety import sha


def minimal_plan():
    return {'schema':'iteration.check-plan/1','kind':'cli','features':[], 'continuation':False,
            'cases':[{'id':'fixture-startup','phase':'startup','category':'startup','description':'Exercise this isolated protocol fixture startup.'},
                     {'id':'fixture-actions','phase':'regression','category':'primary','description':'Exercise the real assertions in this test fixture.'}],
            'not_applicable':{'invalid-input':'This is a gate protocol unit fixture, not a user input application.',
                              'boundary':'This is a gate protocol unit fixture; independent boundary tests exist separately.'}}


def ready_source(source):
    return 'from Automation.RT42 import ready\nready()\n'+source


def traced_source(source):
    import textwrap
    prefix = "from Automation.RT42 import ready, case\nimport sys\nready()\n_phase = '--iteration-smoke-test' in sys.argv\nwith case('fixture-startup' if _phase else 'fixture-actions', 'startup' if _phase else 'primary'):\n"
    return prefix + textwrap.indent(textwrap.dedent(source), '    ')


def rewrite_archive(raw, changes=None, transform=None):
    """Test-only hash-consistent rewrites to challenge trusted-template gates."""
    with zipfile.ZipFile(io.BytesIO(raw)) as z: files={n:z.read(n) for n in z.namelist()}
    if changes:
        for p,v in changes.items():
            if v is None: files.pop(p,None)
            else: files[p]=v
    if transform: transform(files)
    m=json.loads(files[INDEX]);m['file_sha256']={p:sha(d) for p,d in files.items() if p!=INDEX}
    files[INDEX]=json.dumps(m,indent=2).encode()
    out=io.BytesIO()
    with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
        for p,d in sorted(files.items()):z.writestr(p,d)
    return out.getvalue()
