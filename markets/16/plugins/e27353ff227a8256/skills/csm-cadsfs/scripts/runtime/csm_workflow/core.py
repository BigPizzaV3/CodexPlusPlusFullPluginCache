"""Flujo local de integración, independiente del cookbook y del transporte.

No expone red, no llama a modelos, no interpreta imágenes y no autentica usuarios.
Los adaptadores de generación, validación, identidad y entrega real se conectan
por separado. El generador y el validador son código de confianza del propietario;
no se seleccionan ni se cargan desde un argumento del usuario.
"""
from __future__ import annotations

import hashlib
import ipaddress
import json
import math
import os
import re
import secrets
import stat
import tempfile
import threading
import time
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Mapping, Protocol
from urllib.parse import urlsplit

MAX_REQUEST_BYTES = 256_000
MAX_ARTIFACT_BYTES = 32 * 1024 * 1024
MESSAGES = {
    "INVALID_REQUEST": "Faltan datos válidos para preparar el proyecto.",
    "CONFLICTING_DATA": "Hay medidas o datos contradictorios que deben resolverse antes de generar el proyecto.",
    "ASSUMPTIONS_NOT_ALLOWED": "La información disponible requiere estimaciones y este pedido no las autoriza.",
    "ENGINE_UNAVAILABLE": "El generador CSM todavía no está conectado; no se ha creado ningún archivo.",
    "VALIDATOR_UNAVAILABLE": "La validación CSM todavía no está conectada; no se ha entregado ningún archivo.",
    "GENERATION_FAILED": "No se pudo completar la generación del proyecto.",
    "VALIDATION_FAILED": "El proyecto no superó la validación y no se entrega como válido.",
    "INVALID_ARTIFACT": "El archivo obtenido no cumple las condiciones de entrega.",
    "ARTIFACT_UNAVAILABLE": "Ese archivo no está disponible en esta conversación o ha caducado.",
    "CAPACITY_EXCEEDED": "La capacidad temporal de almacenamiento está completa; no se ha publicado el archivo.",
}


class WorkflowError(Exception):
    """Error público enumerado: nunca transporta trazas, rutas ni texto del motor."""
    def __init__(self, code: str):
        if code not in MESSAGES:
            code = "GENERATION_FAILED"
        self.code = code
        super().__init__(MESSAGES[code])


def _invalid() -> None:
    raise WorkflowError("INVALID_REQUEST")


def _keys(data: Any, allowed: set[str], required: set[str]) -> dict[str, Any]:
    if not isinstance(data, dict) or not required <= data.keys() or data.keys() - allowed:
        _invalid()
    return data


def _text(value: Any, limit: int, *, empty: bool = False) -> str:
    if not isinstance(value, str) or len(value) > limit or (not empty and not value.strip()):
        _invalid()
    if "\x00" in value:
        _invalid()
    return value.strip()


def _id(value: Any) -> str:
    value = _text(value, 160)
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.:-]{0,159}", value):
        _invalid()
    return value


def _bool(value: Any) -> bool:
    if type(value) is not bool:
        _invalid()
    return value


def _scalar(value: Any) -> str | int | float | bool:
    if type(value) not in (str, int, float, bool):
        _invalid()
    if isinstance(value, str):
        return _text(value, 4000)
    if type(value) in (float, int):
        if abs(value) > 1e100 or not math.isfinite(value):
            _invalid()
    return value


def _source_url(value: Any) -> str:
    """Filtro de referencias, NO autorización de descarga ni defensa SSRF completa.

    Este módulo jamás descarga la URL. Un futuro descargador necesitará controles
    propios sobre resolución DNS, redirecciones, destinos, tamaño y formato.
    """
    value = _text(value, 2048)
    if any(ord(c) < 33 or ord(c) == 127 for c in value) or "\\" in value:
        _invalid()
    try:
        url = urlsplit(value)
        _ = url.port
        host = url.hostname
        if url.scheme not in ("http", "https") or not host or url.username or url.password:
            _invalid()
        lowered = host.lower().rstrip(".")
        if lowered == "localhost" or lowered.endswith((".localhost", ".local", ".internal")):
            _invalid()
        try:
            ip = ipaddress.ip_address(lowered)
        except ValueError:
            ip = None
        if ip is not None and not ip.is_global:
            _invalid()
    except (ValueError, UnicodeError):
        _invalid()
    return value


def load_request_json(text: str) -> dict[str, Any]:
    """JSON estricto: rechaza claves duplicadas, NaN/Infinity y cargas excesivas."""
    if not isinstance(text, str) or len(text.encode("utf-8")) > MAX_REQUEST_BYTES:
        _invalid()

    def pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in items:
            if key in result:
                _invalid()
            result[key] = value
        return result

    def constant(_: str) -> None:
        _invalid()

    try:
        data = json.loads(text, object_pairs_hook=pairs, parse_constant=constant)
    except (ValueError, RecursionError):
        _invalid()
    if not isinstance(data, dict):
        _invalid()
    return data


@dataclass(frozen=True)
class Source:
    source_id: str
    kind: str
    reference: str
    locator: str

    @classmethod
    def parse(cls, raw: Any) -> Source:
        d = _keys(raw, {"id", "kind", "reference", "locator"}, {"id", "kind", "reference"})
        kind = d["kind"]
        if kind not in ("text", "image", "web", "project"):
            _invalid()
        reference = _source_url(d["reference"]) if kind == "web" else _id(d["reference"])
        return cls(_id(d["id"]), kind, reference, _text(d.get("locator", ""), 400, empty=True))


_LENGTH_FACTORS = {"m": 1.0, "cm": 0.01, "mm": 0.001, "ft": 0.3048, "in": 0.0254}
_UNITS = set(_LENGTH_FACTORS) | {"m2", "m3", "deg", "Hz", "dB", "%", "count"}
_POSITIVE_DIMENSIONS = {"room.length", "room.width", "room.height", "stage.width", "stage.depth"}


@dataclass(frozen=True)
class Fact:
    key: str
    value: str | int | float | bool
    unit: str | None
    basis: str
    source_ids: tuple[str, ...]
    note: str

    @classmethod
    def parse(cls, raw: Any, available_sources: set[str]) -> Fact:
        d = _keys(raw, {"key", "value", "unit", "basis", "source_ids", "note"},
                  {"key", "value", "basis", "source_ids"})
        key = _id(d["key"])
        value = _scalar(d["value"])
        unit = d.get("unit")
        if unit is not None and (not isinstance(unit, str) or unit not in _UNITS):
            _invalid()
        if unit is not None and type(value) not in (int, float):
            _invalid()
        if key in _POSITIVE_DIMENSIONS:
            if type(value) not in (int, float) or value <= 0 or unit not in _LENGTH_FACTORS:
                _invalid()
        if unit == "count" and (type(value) is not int or value < 0):
            _invalid()
        basis = d["basis"]
        if basis not in ("user", "documented", "assumption"):
            _invalid()
        ids = d["source_ids"]
        if not isinstance(ids, list) or len(ids) > 100:
            _invalid()
        refs = tuple(_id(item) for item in ids)
        if len(set(refs)) != len(refs) or not set(refs) <= available_sources:
            _invalid()
        if basis != "assumption" and not refs:
            _invalid()
        note = _text(d.get("note", ""), 2000, empty=True)
        if basis == "assumption" and not note:
            _invalid()
        return cls(key, value, unit, basis, refs, note)

    def canonical(self) -> tuple[str, Any]:
        if self.unit in _LENGTH_FACTORS:
            return ("m", float(self.value) * _LENGTH_FACTORS[self.unit])
        return (self.unit or type(self.value).__name__, self.value)


def _same_fact(a: Fact, b: Fact) -> bool:
    ua, va = a.canonical()
    ub, vb = b.canonical()
    if ua != ub:
        return False
    if type(va) in (float, int) and type(vb) in (float, int):
        return math.isclose(va, vb, rel_tol=1e-9, abs_tol=1e-9)
    return type(va) is type(vb) and va == vb


@dataclass(frozen=True)
class ProjectRequest:
    title: str
    instruction: str
    operation: str
    allow_assumptions: bool
    sources: tuple[Source, ...]
    facts: tuple[Fact, ...]
    requirements: tuple[str, ...]
    base_artifact_id: str | None

    @classmethod
    def parse(cls, raw: Any) -> ProjectRequest:
        try:
            size = len(json.dumps(raw, allow_nan=False).encode("utf-8"))
        except (ValueError, TypeError, RecursionError, OverflowError):
            _invalid()
        if size > MAX_REQUEST_BYTES:
            _invalid()
        d = _keys(raw, {"title", "instruction", "operation", "allow_assumptions", "sources", "facts",
                        "requirements", "base_artifact_id"},
                  {"title", "instruction", "operation", "allow_assumptions", "sources", "facts"})
        if d["operation"] not in ("create", "edit"):
            _invalid()
        assumptions = _bool(d["allow_assumptions"])
        if not isinstance(d["sources"], list) or len(d["sources"]) > 100:
            _invalid()
        sources = tuple(Source.parse(s) for s in d["sources"])
        ids = {s.source_id for s in sources}
        if len(ids) != len(sources):
            _invalid()
        if not isinstance(d["facts"], list) or len(d["facts"]) > 1000:
            _invalid()
        facts = tuple(Fact.parse(f, ids) for f in d["facts"])
        seen: dict[str, Fact] = {}
        for fact in facts:
            if fact.key in seen and not _same_fact(fact, seen[fact.key]):
                raise WorkflowError("CONFLICTING_DATA")
            seen[fact.key] = fact
        if not assumptions and any(f.basis == "assumption" for f in facts):
            raise WorkflowError("ASSUMPTIONS_NOT_ALLOWED")
        requirements = d.get("requirements", [])
        if not isinstance(requirements, list) or len(requirements) > 100:
            _invalid()
        base = d.get("base_artifact_id")
        if base is not None:
            base = _id(base)
        if (d["operation"] == "edit") != (base is not None):
            _invalid()
        return cls(_text(d["title"], 120), _text(d["instruction"], 32000), d["operation"], assumptions,
                   sources, facts, tuple(_text(r, 2000) for r in requirements), base)


@dataclass(frozen=True)
class AccessContext:
    """Sólo lo construye el adaptador de identidad de confianza, nunca el modelo.

    Estos valores no autentican por sí mismos a nadie. El transporte real deberá
    comprobar credenciales y asociar la conversación antes de llamar al núcleo.
    """
    principal: str
    conversation: str

    def __post_init__(self) -> None:
        _id(self.principal)
        _id(self.conversation)


@dataclass(frozen=True)
class ValidationReport:
    """Lo emite un validador REAL, no el modelo ni una respuesta textual del chat.

    content_safe: comprobación dependiente del formato que excluye código,
    cookbook, metadatos privados y contenido impropio dentro del CSM.
    """
    structure: bool
    geometry: bool
    requirements: bool
    content_safe: bool
    edit_preserved: bool | None = None
    opened_in_cadsfs: bool = False

    def passed(self, editing: bool) -> bool:
        flags = (self.structure, self.geometry, self.requirements, self.content_safe)
        return all(flag is True for flag in flags) and (not editing or self.edit_preserved is True)


class Generator(Protocol):
    def generate(self, request: ProjectRequest, base_project: bytes | None, workdir: Path) -> Path:
        """Escribe el resultado en workdir y devuelve su ruta; no retorna secretos."""
        ...


class Validator(Protocol):
    def validate(self, content: bytes, request: ProjectRequest, base_project: bytes | None) -> ValidationReport:
        """Valida contenido real, fidelidad al pedido y diferencias de una edición."""
        ...


@dataclass(frozen=True)
class Artifact:
    artifact_id: str
    filename: str
    content: bytes
    sha256: str
    created_at: float
    expires_at: float
    context: AccessContext
    notices: tuple[str, ...]
    opened_in_cadsfs: bool


class MemoryArtifactStore:
    """Almacén de DESARROLLO, en memoria, con caducidad y cuota global.

    No es almacenamiento de producción ni autenticación. No genera URLs. Su
    aislamiento sólo es válido si AccessContext procede de identidad verificada.
    La expiración elimina referencias en memoria, no asegura borrado forense.
    """
    def __init__(self, ttl_seconds: float = 3600, capacity_bytes: int = 64 * 1024 * 1024,
                 clock: Callable[[], float] = time.time):
        if type(ttl_seconds) not in (int, float) or not math.isfinite(ttl_seconds) or ttl_seconds <= 0:
            raise ValueError("ttl_seconds debe ser positivo y finito")
        if type(capacity_bytes) is not int or capacity_bytes <= 0:
            raise ValueError("capacity_bytes debe ser un entero positivo")
        self.ttl = ttl_seconds
        self.capacity = capacity_bytes
        self.clock = clock
        self._items: dict[str, Artifact] = {}
        self._lock = threading.RLock()

    def _purge(self) -> None:
        now = self.clock()
        for key in list(self._items):
            if self._items[key].expires_at <= now:
                del self._items[key]

    def put(self, ctx: AccessContext, filename: str, content: bytes, notices: tuple[str, ...],
            opened_in_cadsfs: bool) -> Artifact:
        if type(content) is not bytes or not content or len(content) > MAX_ARTIFACT_BYTES:
            raise WorkflowError("INVALID_ARTIFACT")
        with self._lock:
            self._purge()
            if sum(len(a.content) for a in self._items.values()) + len(content) > self.capacity:
                raise WorkflowError("CAPACITY_EXCEEDED")
            now = self.clock()
            artifact_id = "csm_" + secrets.token_hex(16)
            while artifact_id in self._items:
                artifact_id = "csm_" + secrets.token_hex(16)
            result = Artifact(artifact_id, filename, content, hashlib.sha256(content).hexdigest(), now,
                              now + self.ttl, ctx, notices, opened_in_cadsfs is True)
            self._items[artifact_id] = result
            return result

    def get(self, ctx: AccessContext, artifact_id: str) -> Artifact:
        with self._lock:
            self._purge()
            result = self._items.get(artifact_id)
            if result is None or result.context != ctx:
                raise WorkflowError("ARTIFACT_UNAVAILABLE")
            return result

    def delete(self, ctx: AccessContext, artifact_id: str) -> None:
        with self._lock:
            result = self.get(ctx, artifact_id)
            del self._items[result.artifact_id]


def _safe_filename(title: str) -> str:
    ascii_title = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode()
    stem = re.sub(r"[^A-Za-z0-9_-]+", "_", ascii_title).strip("_-")[:72] or "Sala"
    if stem.upper() in {"CON", "PRN", "AUX", "NUL", *(f"COM{i}" for i in range(1, 10)),
                        *(f"LPT{i}" for i in range(1, 10))}:
        stem = "Sala_" + stem
    return stem + ".csm"


def _read_candidate(path: Path, workdir: Path) -> bytes:
    """Acepta UN archivo regular .csm dentro del directorio aislado del trabajo.

    No inspecciona sintaxis CSM. Esa función corresponde al Validator.
    No es un sandbox para ejecutar código de un atacante.
    """
    try:
        p = Path(path)
        root = workdir.resolve(strict=True)
        if not p.is_absolute():
            p = workdir / p
        # No se aceptan '..', symlinks en el archivo o sus directorios, ni rutas externas.
        if ".." in p.parts:
            raise WorkflowError("INVALID_ARTIFACT")
        p.relative_to(root)
        for node in (p, *p.parents):
            if node == root:
                break
            if node.is_symlink():
                raise WorkflowError("INVALID_ARTIFACT")
        resolved = p.resolve(strict=True)
        resolved.relative_to(root)
        if resolved.suffix != ".csm":
            raise WorkflowError("INVALID_ARTIFACT")
        flags = (os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_BINARY", 0)
                 | getattr(os, "O_NONBLOCK", 0))
        descriptor = os.open(resolved, flags)
        with os.fdopen(descriptor, "rb") as stream:
            info = os.fstat(stream.fileno())
            if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1 or not 0 < info.st_size <= MAX_ARTIFACT_BYTES:
                raise WorkflowError("INVALID_ARTIFACT")
            content = stream.read(MAX_ARTIFACT_BYTES + 1)
        if not content or len(content) > MAX_ARTIFACT_BYTES or not content.strip():
            raise WorkflowError("INVALID_ARTIFACT")
        if content.startswith((b"PK\x03\x04", b"MZ", b"%PDF-", b"\x89PNG", b"\xff\xd8\xff", b"\x1f\x8b")):
            raise WorkflowError("INVALID_ARTIFACT")
        return content
    except WorkflowError:
        raise
    except (OSError, ValueError, TypeError):
        raise WorkflowError("INVALID_ARTIFACT") from None


@dataclass(frozen=True)
class Outcome:
    ok: bool
    code: str
    artifact_id: str | None = None
    filename: str | None = None
    size_bytes: int | None = None
    sha256: str | None = None
    expires_at: float | None = None
    notices: tuple[str, ...] = ()
    opened_in_cadsfs: bool = False

    def public_payload(self) -> dict[str, Any]:
        if not self.ok:
            return {"ok": False, "code": self.code, "message": MESSAGES[self.code]}
        # Sin contenido CSM, rutas, trazas, cookbook ni datos del usuario autenticado.
        return {"ok": True, "artifact_id": self.artifact_id, "filename": self.filename,
                "size_bytes": self.size_bytes, "sha256": self.sha256, "expires_at": self.expires_at,
                "notices": list(self.notices), "opened_in_cadsfs": self.opened_in_cadsfs}


class Workflow:
    """Orquestación síncrona y sin transporte. No publica ni crea enlaces."""
    def __init__(self, store: MemoryArtifactStore, generator: Generator | None = None,
                 validator: Validator | None = None):
        self.store, self.generator, self.validator = store, generator, validator

    def run(self, ctx: AccessContext, raw_request: Mapping[str, Any]) -> Outcome:
        try:
            req = ProjectRequest.parse(raw_request)
            base = self.store.get(ctx, req.base_artifact_id).content if req.base_artifact_id else None
            if self.generator is None:
                raise WorkflowError("ENGINE_UNAVAILABLE")
            if self.validator is None:
                raise WorkflowError("VALIDATOR_UNAVAILABLE")
            with tempfile.TemporaryDirectory(prefix="csm_job_") as directory:
                root = Path(directory).resolve()
                try:
                    candidate = self.generator.generate(req, base, root)
                except Exception:
                    # Tampoco confiar en el texto/código de excepciones del adaptador.
                    raise WorkflowError("GENERATION_FAILED") from None
                content = _read_candidate(candidate, root)
                try:
                    report = self.validator.validate(content, req, base)
                except Exception:
                    raise WorkflowError("VALIDATION_FAILED") from None
                if not isinstance(report, ValidationReport) or not report.passed(req.operation == "edit"):
                    raise WorkflowError("VALIDATION_FAILED")
                notices = ("Geometría o datos parcialmente estimados; no constituye un relevamiento.",) \
                    if any(f.basis == "assumption" for f in req.facts) else ()
                artifact = self.store.put(ctx, _safe_filename(req.title), content, notices, report.opened_in_cadsfs)
            return Outcome(True, "OK", artifact.artifact_id, artifact.filename, len(content), artifact.sha256,
                           artifact.expires_at, artifact.notices, artifact.opened_in_cadsfs)
        except WorkflowError as exc:
            return Outcome(False, exc.code)
        except Exception:
            return Outcome(False, "GENERATION_FAILED")


@dataclass(frozen=True)
class VerifiedDownload:
    """Recibo emitido por el ADAPTADOR DE ENTREGA, no por el modelo.

    Su mera construcción NO prueba una descarga. El adaptador futuro deberá subir
    el mismo contenido, comprobar accesibilidad/autorización y aportar su referencia
    real. El núcleo sólo coteja esa atestación y restringe el destino del enlace.
    """
    artifact_id: str
    sha256: str
    url: str


def render_delivery(outcome: Outcome, receipt: VerifiedDownload | None = None,
                    allowed_origins: frozenset[str] = frozenset()) -> str:
    """Respuesta breve; no construye URLs ni transforma IDs en enlaces supuestos."""
    if not outcome.ok:
        return MESSAGES[outcome.code]
    if (receipt is None or receipt.artifact_id != outcome.artifact_id or receipt.sha256 != outcome.sha256):
        raise WorkflowError("ARTIFACT_UNAVAILABLE")
    url = receipt.url
    if not isinstance(url, str) or any(c in url for c in "\r\n\t ()<>\\"):
        raise WorkflowError("ARTIFACT_UNAVAILABLE")
    if any(ord(c) < 33 or ord(c) == 127 for c in url):
        raise WorkflowError("ARTIFACT_UNAVAILABLE")
    try:
        parsed = urlsplit(url)
        _ = parsed.port
        if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password:
            raise WorkflowError("ARTIFACT_UNAVAILABLE")
        origin = f"https://{parsed.netloc}"
        if origin not in allowed_origins:
            raise WorkflowError("ARTIFACT_UNAVAILABLE")
    except ValueError:
        raise WorkflowError("ARTIFACT_UNAVAILABLE") from None
    label = outcome.filename or "Proyecto.csm"
    if not re.fullmatch(r"[A-Za-z0-9_-]+\.csm", label):
        raise WorkflowError("INVALID_ARTIFACT")
    lines = [f"[Descargar {label}]({url})", "Proyecto generado y validado por el motor configurado."]
    lines.extend(outcome.notices[:1])
    return "\n\n".join(lines)
