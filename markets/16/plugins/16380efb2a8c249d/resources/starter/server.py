"""Standalone HTTP API for template-based ZIP generation and download."""
import base64, os, secrets, time
from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel, Field
from generator import TemplateError, generate, inspect_template

app = FastAPI(title='Integration Flow Builder', version='0.1.0')
ARTIFACTS: dict[str, tuple[bytes, float, str]] = {}
TTL_SECONDS = 900
MAX_INPUT = 10 * 1024 * 1024

class BuildRequest(BaseModel):
    template_zip_base64: str = Field(description='Base64 encoding of a genuine SAP-exported iFlow ZIP')
    technical_id: str
    display_name: str
    description: str = ''
    scripts: dict[str, str] = Field(default_factory=dict)

@app.get('/health')
def health():
    return {'status':'ok','service':'Integration Flow Builder','version':'0.1.0'}

@app.post('/inspect')
def inspect(body: dict):
    try:
        data = base64.b64decode(body['template_zip_base64'], validate=True)
        if len(data) > MAX_INPUT: raise TemplateError('Template too large')
        return inspect_template(data)
    except (TemplateError, ValueError, KeyError) as exc:
        raise HTTPException(400, str(exc))

@app.post('/generate')
def build(req: BuildRequest):
    try:
        data = base64.b64decode(req.template_zip_base64, validate=True)
        if len(data) > MAX_INPUT: raise TemplateError('Template too large')
        archive, report = generate(data, req.technical_id, req.display_name, req.description, req.scripts)
    except (ValueError, TemplateError) as exc:
        raise HTTPException(400, str(exc))
    for key, (_, created, _) in list(ARTIFACTS.items()):
        if time.time() - created > TTL_SECONDS: ARTIFACTS.pop(key, None)
    key = secrets.token_urlsafe(24)
    ARTIFACTS[key] = (archive, time.time(), req.technical_id)
    return {'download_path':'/download/'+key,'filename':req.technical_id+'.zip','validation':report, 'expires_in_seconds':TTL_SECONDS}

@app.get('/download/{token}')
def download(token: str):
    item = ARTIFACTS.get(token)
    if item is None or time.time() - item[1] > TTL_SECONDS:
        ARTIFACTS.pop(token, None)
        raise HTTPException(404, 'File expired or unavailable')
    data, _, name = item
    return Response(data, media_type='application/zip', headers={'Content-Disposition':f'attachment; filename="{name}.zip"','Cache-Control':'no-store'})
