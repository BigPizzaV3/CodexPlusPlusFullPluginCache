#!/usr/bin/env python3
"""Offline, bounded Whisper transcription. No installation, downloads or API calls.

Requires PyAV, NumPy, and either openai-whisper/PyTorch or faster-whisper, with an
explicitly provided local model. The checkpoint must be trusted: PyTorch loading is not
a safe way to inspect untrusted files. Run in the user's working area, not inside
a distributable plugin. Japanese is the default language; original wording is
retained. Warnings identify review candidates, not proven recognition errors.
"""
import argparse
import collections
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import re
import sys
import tempfile

VERSION = "0.2.0"
MAX_DEFAULT_SECONDS = 7200.0
CHUNK_SECONDS = 600.0


class TrialError(Exception):
    def __init__(self, code, message):
        super().__init__(message)
        self.code = code


def dependencies(backend="whisper"):
    packages = {"av": "av", "numpy": "numpy"}
    packages.update({"faster_whisper": "faster-whisper"} if backend == "faster-whisper" else {"whisper": "openai-whisper", "torch": "torch"})
    return {package: {"available": importlib.util.find_spec(module) is not None,
                      "module": module} for module, package in packages.items()}


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def select_backend(requested, model_path, model_cache, model):
    if requested != "auto":
        return requested
    if model_path:
        return "faster-whisper" if Path(model_path).expanduser().is_dir() else "whisper"
    if model_cache and (Path(model_cache).expanduser() / (model + ".pt")).is_file():
        return "whisper"
    return "faster-whisper" if importlib.util.find_spec("faster_whisper") else "whisper"


def resolve_model(model, model_path, model_cache, backend="whisper"):
    if bool(model_path) == bool(model_cache):
        raise TrialError("missing_model_location", "Specify exactly one --model-path or --model-cache. No model is downloaded automatically.")
    if model_path:
        path = Path(model_path).expanduser().resolve()
    else:
        if not re.fullmatch(r"[A-Za-z0-9_.-]+", model) or model in (".", ".."):
            raise TrialError("invalid_model_name", "--model must be a checkpoint name, not a path.")
        filename = "faster-whisper-" + model if backend == "faster-whisper" else model + ".pt"
        path = Path(model_cache).expanduser().resolve() / filename
    if backend == "faster-whisper":
        required = ("model.bin", "config.json", "tokenizer.json")
        if not path.is_dir() or any(not (path / name).is_file() or not (path / name).stat().st_size for name in required):
            raise TrialError("missing_model", "faster-whisper requires a local model directory containing nonempty model.bin, config.json, and tokenizer.json: " + str(path))
    elif not path.is_file() or path.stat().st_size == 0:
        raise TrialError("missing_model", "A nonempty trusted local Whisper .pt checkpoint is required: " + str(path))
    return path


def model_hash(path):
    if path.is_file():
        return sha256(path)
    # Only known runtime files; do not enumerate unrelated content in the folder.
    hashes = {name: sha256(path / name) for name in ("model.bin", "config.json", "tokenizer.json", "preprocessor_config.json", "vocabulary.json", "vocabulary.txt") if (path / name).is_file()}
    return hashlib.sha256(json.dumps(hashes, sort_keys=True).encode("utf-8")).hexdigest()


def validate_output_directory(path):
    # Protect distribution trees without prohibiting a separate release QA area.
    resolved = path.expanduser().resolve()
    for ancestor in (resolved,) + tuple(resolved.parents):
        if (ancestor / ".codex-plugin").is_dir() or (ancestor / ".claude-plugin").is_dir() or (ancestor / "plugin.json").is_file():
            raise TrialError("plugin_output_forbidden", "Store personal audio/transcripts outside a plugin distribution tree.")
    if resolved.exists():
        raise TrialError("output_exists", "--out-dir must be a new directory; existing files are never overwritten: " + str(resolved))
    return resolved


def decode_audio(path, max_seconds, decoded_path=None):
    """Decode the complete file. A private scratch path keeps long recordings off RAM."""
    import av
    import numpy as np
    if not math.isfinite(max_seconds) or max_seconds <= 0:
        raise TrialError("invalid_limit", "--max-seconds must be finite and positive.")
    chunks = []
    total = 0
    sum_squares = 0.0
    limit = int(max_seconds * 16000)
    sink = Path(decoded_path).open("xb") if decoded_path else None

    def append(converted):
        nonlocal total, sum_squares
        samples = converted.to_ndarray().reshape(-1).astype(np.float32, copy=False)
        if not np.isfinite(samples).all():
            raise TrialError("invalid_samples", "Decoded audio contains non-finite samples.")
        total += samples.size
        if total > limit:
            raise TrialError("duration_limit", "Decoded audio exceeds --max-seconds; no partial transcript was produced.")
        sum_squares += float(np.sum(np.square(samples.astype(np.float64))))
        if sink:
            sink.write(samples.tobytes())
        else:
            chunks.append(samples)

    try:
        with av.open(str(path)) as container:
            if not container.streams.audio:
                raise TrialError("no_audio_stream", "The supplied file has no decodable audio stream.")
            source_audio_streams = len(container.streams.audio)
            stream = container.streams.audio[0]
            declared = float(stream.duration * stream.time_base) if stream.duration is not None and stream.time_base else None
            if declared is not None and declared > max_seconds + 0.1:
                raise TrialError("duration_limit", "Audio exceeds --max-seconds; raise the processing limit or split it in the task runtime.")
            resampler = av.AudioResampler(format="fltp", layout="mono", rate=16000)
            for frame in container.decode(stream):
                for converted in resampler.resample(frame):
                    append(converted)
            for converted in resampler.resample(None):
                append(converted)
    except TrialError:
        raise
    except Exception as exc:
        raise TrialError("decode_failed", "PyAV could not decode this local file: " + str(exc)) from exc
    finally:
        if sink:
            sink.close()
    if not total:
        raise TrialError("empty_audio", "No audio samples were decoded.")
    audio = np.memmap(str(decoded_path), dtype="float32", mode="r", shape=(total,)) if decoded_path else np.concatenate(chunks)
    return audio, {"duration_seconds": total / 16000.0, "sample_rate_hz": 16000,
                   "channels": 1, "sample_count": int(total), "rms": math.sqrt(sum_squares / total),
                   "source_audio_streams": source_audio_streams}


def transcribe_chunks(model, audio, backend, language, chunk_seconds=CHUNK_SECONDS):
    """Bound inference memory and retain global times and every recognized segment.

    Chunks cover the full sample interval without gaps. Boundaries may split a
    word; mark their nearby segments rather than silently rewriting the wording.
    """
    import numpy as np
    if not math.isfinite(chunk_seconds) or not 30 <= chunk_seconds <= 600:
        raise TrialError("invalid_chunk_limit", "--chunk-seconds must be from 30 to 600.")
    step = int(chunk_seconds * 16000)
    records, windows = [], []
    for first in range(0, len(audio), step):
        last = min(first + step, len(audio))
        start_seconds, end_seconds = first / 16000.0, last / 16000.0
        part = audio[first:last]
        # A voiced recording can contain entire silent later chunks. Do not let
        # Whisper invent a closing phrase on such a chunk.
        chunk_rms = float(np.sqrt(np.mean(np.square(part))))
        if chunk_rms < 1e-7:
            windows.append({"start": start_seconds, "end": end_seconds, "sample_count": last - first,
                            "recognition": "skipped_silence", "rms": chunk_rms})
            print(json.dumps({"event": "chunk_completed", "processed_audio_seconds": end_seconds,
                              "duration_seconds": len(audio) / 16000.0, "recognition": "skipped_silence"}), file=sys.stderr, flush=True)
            continue
        if backend == "faster-whisper":
            stream, _ = model.transcribe(part, language=language, task="transcribe",
                                        beam_size=1, best_of=1, temperature=0.0,
                                        condition_on_previous_text=False, vad_filter=False,
                                        no_speech_threshold=0.6, log_prob_threshold=-1.0,
                                        compression_ratio_threshold=2.4)
            current = [{key: getattr(segment, key) for key in ("id", "start", "end", "text", "avg_logprob", "no_speech_prob", "compression_ratio")} for segment in stream]
        else:
            result = model.transcribe(part, language=language, task="transcribe", fp16=False,
                                      verbose=None, temperature=0.0, condition_on_previous_text=False,
                                      no_speech_threshold=0.6, logprob_threshold=-1.0,
                                      compression_ratio_threshold=2.4)
            current = result.get("segments", [])
        # Validate in each chunk's coordinate system before applying its offset.
        _, validated, _, _ = validate_result({"text": "".join(s.get("text", "") for s in current), "segments": current}, end_seconds - start_seconds)
        for raw in validated:
            segment = dict(raw)
            segment["id"] = len(records)
            segment["chunk_index"] = len(windows)
            for key in ("start", "end"):
                if isinstance(segment[key], (int, float)):
                    segment[key] += start_seconds
            segment["near_chunk_boundary"] = bool(
                len(audio) > step and isinstance(segment["start"], (int, float)) and isinstance(segment["end"], (int, float)) and
                ((first > 0 and segment["start"] < start_seconds + 1.0) or
                 (last < len(audio) and segment["end"] > end_seconds - 1.0)))
            records.append(segment)
        windows.append({"start": start_seconds, "end": end_seconds, "sample_count": last - first,
                        "recognition": "transcribed", "rms": chunk_rms})
        print(json.dumps({"event": "chunk_completed", "processed_audio_seconds": end_seconds,
                          "duration_seconds": len(audio) / 16000.0}), file=sys.stderr, flush=True)
    return {"text": "".join(s["text"] for s in records), "segments": records}, windows


def timeline_coverage(segments, duration):
    """Measure union of recognized segment windows; this is not voice activity."""
    intervals = []
    for segment in segments:
        start, end = segment.get("start"), segment.get("end")
        if isinstance(start, (int, float)) and isinstance(end, (int, float)) and math.isfinite(start) and math.isfinite(end) and 0 <= start <= end <= duration + 0.25 and segment.get("text", "").strip():
            intervals.append((min(start, duration), min(end, duration)))
    merged = []
    for start, end in sorted(intervals):
        if merged and start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    covered = sum(end - start for start, end in merged)
    leading = merged[0][0] if merged else duration
    trailing = duration - merged[-1][1] if merged else 0.0
    internal_gaps = [merged[i][0] - merged[i - 1][1] for i in range(1, len(merged))]
    max_internal = max(internal_gaps, default=0.0)
    uncovered = max(0.0, duration - covered)
    large_gap = max(leading, trailing, max_internal) >= max(20.0, duration * 0.1)
    substantial_uncovered = uncovered >= max(30.0, duration * 0.25)
    return {"leading_gap_seconds": leading, "trailing_gap_seconds": trailing,
            "max_internal_gap_seconds": max_internal, "uncovered_seconds": uncovered,
            "spoken_segment_seconds": covered, "segment_window_coverage_ratio": covered / duration if duration else 0.0,
            "large_gap_requires_review": large_gap or substantial_uncovered,
            "speech_completeness_verified": False,
            "meaning": "Union of recognized segment timestamp windows, not measured speech duration. Gaps may be silence or omitted speech; coverage alone cannot distinguish them."}


def validate_result(result, duration):
    """Preserve text, flag unreliable output, never claim semantic verification."""
    text = result.get("text", "")
    if not isinstance(text, str):
        raise TrialError("invalid_result", "Transcriber returned non-text output.")
    segments = []
    warnings = []
    repeated = collections.Counter()
    invalid_timing = False
    previous_start = None
    previous_max_end = None
    for index, raw in enumerate(result.get("segments", [])):
        segment = {key: raw.get(key) for key in ("id", "start", "end", "text", "avg_logprob", "no_speech_prob", "compression_ratio")}
        if "chunk_index" in raw:
            segment["chunk_index"] = raw["chunk_index"]
        if not isinstance(segment["text"], str):
            raise TrialError("invalid_result", "A transcript segment contains non-text content.")
        segment["id"] = index
        flags = list(raw.get("review_flags", []))
        if raw.get("near_chunk_boundary"):
            flags.append("chunk_boundary")
        start, end = segment["start"], segment["end"]
        if any(isinstance(value, (int, float)) and not math.isfinite(value) for value in (start, end)):
            raise TrialError("nonfinite_backend_result", "Segment %d has a non-finite timestamp; transcription is unusable." % index)
        if not isinstance(start, (int, float)) or not isinstance(end, (int, float)) or not math.isfinite(start) or not math.isfinite(end) or start < 0 or end < start or end > duration + 0.25:
            flags.append("invalid_timestamps")
            invalid_timing = True
        else:
            if previous_start is not None and start < previous_start - 0.01:
                flags.append("out_of_order_timestamps")
            if previous_max_end is not None and start < previous_max_end - 0.25:
                flags.append("overlapping_timestamps")
            previous_start = start
            previous_max_end = max(previous_max_end or 0.0, end)
        for key, test, flag in (("avg_logprob", lambda v: v < -1.0, "low_confidence"),
                                ("no_speech_prob", lambda v: v >= 0.6, "possible_no_speech"),
                                ("compression_ratio", lambda v: v > 2.4, "possible_repetition")):
            value = segment[key]
            if value is not None and (not isinstance(value, (int, float)) or not math.isfinite(value)):
                raise TrialError("nonfinite_backend_result", "Segment %d has invalid %s; do not use this transcription. Check the backend numerical runtime." % (index, key))
            if isinstance(value, (int, float)) and math.isfinite(value) and test(value):
                flags.append(flag)
        normalized = re.sub(r"[\s\W]+", "", segment["text"], flags=re.UNICODE)
        if len(normalized) >= 8:
            repeated[normalized] += 1
        segment["review_flags"] = flags
        segments.append(segment)
    for segment in segments:
        normalized = re.sub(r"[\s\W]+", "", segment["text"], flags=re.UNICODE)
        if repeated[normalized] >= 3:
            segment["review_flags"].append("repeated_phrase")
    if not text.strip() or not segments or not any(s["text"].strip() for s in segments):
        status = "no_transcript"
        warnings.append("No usable speech transcript was returned. Do not proceed to research from an empty result.")
    elif all(isinstance(s["no_speech_prob"], (int, float)) and s["no_speech_prob"] >= 0.6 for s in segments):
        status = "needs_review"
        warnings.append("Every segment is flagged as possible no-speech; this is not a verified transcript.")
    elif invalid_timing or any(s["review_flags"] for s in segments):
        status = "needs_review"
    else:
        status = "transcribed_unverified"
    if any(s["review_flags"] for s in segments):
        warnings.append("Review flagged timestamps against the recording. Confidence flags cannot prove accuracy or hallucination.")
    if text.strip() and segments and "".join(s["text"] for s in segments).strip() != text.strip():
        warnings.append("Raw full text and concatenated segments differ; both were preserved without cleaning.")
        if status == "transcribed_unverified":
            status = "needs_review"
    coverage = timeline_coverage(segments, duration)
    if coverage["large_gap_requires_review"] and status != "no_transcript":
        warnings.append("Large intervals have no recognized segment. They may be silence or omitted speech; compare the recording before proceeding. This is a review flag, not proof of missing speech or a failed transcription.")
        status = "needs_review"
    return text, segments, status, warnings


def write_outputs(directory, text, report):
    # mkdir and exclusive file modes prevent silent overwrite, including races.
    encoded_report = json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False)
    directory = validate_output_directory(directory)
    directory.mkdir(parents=True, exist_ok=False)
    with (directory / "transcript.raw.txt").open("x", encoding="utf-8") as handle:
        handle.write(text)
    with (directory / "transcript.json").open("x", encoding="utf-8") as handle:
        handle.write(encoded_report)
        handle.write("\n")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Existing local M4A/MP3/WAV or other PyAV-readable file")
    parser.add_argument("--probe", action="store_true", help="Decode and inspect the audio using av/numpy; no model or output directory required")
    parser.add_argument("--out-dir", help="New private output directory outside plugin distribution")
    parser.add_argument("--model", default="small")
    parser.add_argument("--backend", choices=("auto", "whisper", "faster-whisper"), default="auto")
    parser.add_argument("--model-path", help="Trusted local Whisper checkpoint, no download")
    parser.add_argument("--model-cache", help="Explicit existing directory containing <model>.pt")
    parser.add_argument("--language", default="ja")
    parser.add_argument("--threads", type=int, default=2)
    parser.add_argument("--max-seconds", type=float, default=MAX_DEFAULT_SECONDS)
    parser.add_argument("--chunk-seconds", type=float, default=CHUNK_SECONDS)
    parser.add_argument("--max-bytes", type=int, default=1024 * 1024 * 1024)
    args = parser.parse_args(argv)
    backend = select_backend(args.backend, args.model_path, args.model_cache, args.model)
    report = {"schema_version": VERSION, "status": "not_started", "backend": backend,
              "model": args.model, "language": args.language, "dependencies": dependencies(backend),
              "processed_audio_seconds": 0, "processing_complete": False, "network_used": False,
              "processed_audio_seconds_meaning": "Duration of contiguous input chunks with completed engine calls or an effective-silence check. This does not establish recognition of all speech; inspect timeline_coverage and compare the recording.",
              "limitations": ["This is automatic speech recognition, not a verified quotation or medical fact check.",
                              "Names, numbers, medical terms, and negation require comparison with the recording.",
                              "No diarization; only the first audio stream is used.",
                              "Unavailable dependencies/models are reported; nothing is installed or downloaded.",
                              "ChatGPT Web must actually expose an uploaded audio file to a Python runtime with these dependencies and checkpoint; this helper cannot grant that capability."]}
    try:
        path = Path(args.input).expanduser().resolve()
        if not path.is_file():
            raise TrialError("missing_input", "Input must be an existing local file: " + str(path))
        if args.max_bytes <= 0 or path.stat().st_size > args.max_bytes:
            raise TrialError("size_limit", "Input exceeds --max-bytes, or the byte limit is invalid.")
        if not 1 <= args.threads <= 8:
            raise TrialError("invalid_threads", "--threads must be 1 through 8.")
        if not args.probe and not args.out_dir:
            raise TrialError("missing_output", "--out-dir is required unless --probe is used.")
        output = validate_output_directory(Path(args.out_dir)) if args.out_dir else None
        required = {name: info for name, info in report["dependencies"].items() if not args.probe or name in ("av", "numpy")}
        missing = [name for name, info in required.items() if not info["available"]]
        if missing:
            raise TrialError("missing_dependencies", "The runtime requires these installed packages: " + ", ".join(missing) + ". Installation is not performed by this script.")
        report.update({"input_file": path.name, "input_sha256": sha256(path), "input_bytes": path.stat().st_size})
        # OS-private scratch storage is discarded on both success and failure.
        # No decoded recording is written into the distributed skill directory.
        with tempfile.TemporaryDirectory(prefix="dr-shigyo-audio-") as scratch:
            audio, metadata = decode_audio(path, args.max_seconds, Path(scratch) / "decoded.f32")
            try:
                report.update(metadata)
                if metadata["rms"] < 1e-7:
                    report.update({"status": "no_transcript", "reason": "effectively_silent_audio", "segments": [],
                                   "timeline_coverage": timeline_coverage([], metadata["duration_seconds"]),
                                   "warnings": ["Audio is effectively silent; the recognition model was not run."]})
                    if output and not args.probe:
                        report["output_directory"] = str(output)
                        write_outputs(output, "", report)
                    print(json.dumps(report, ensure_ascii=False, allow_nan=False))
                    return 3
                if args.probe:
                    report.update({"status": "audio_ready", "audio_decoded_completely": True,
                                   "readiness_scope": "Audio decoding only; no speech recognition was performed."})
                    print(json.dumps(report, ensure_ascii=False, allow_nan=False))
                    return 0
                model_path = resolve_model(args.model, args.model_path, args.model_cache, backend)
                report.update({"model_checkpoint": model_path.name, "model_sha256": model_hash(model_path)})
                os.environ["OMP_NUM_THREADS"] = str(args.threads)
                os.environ["MKL_NUM_THREADS"] = str(args.threads)
                if backend == "faster-whisper":
                    from faster_whisper import WhisperModel
                    model = WhisperModel(str(model_path), device="cpu", compute_type="int8",
                                         cpu_threads=args.threads, num_workers=1, local_files_only=True)
                    report["compute_type"] = "int8"
                else:
                    import torch
                    import whisper
                    torch.set_num_threads(args.threads)
                    model = whisper.load_model(str(model_path), device="cpu")
                    report["compute_type"] = "float32"
                result, windows = transcribe_chunks(model, audio, backend, args.language, args.chunk_seconds)
                text, segments, status, warnings = validate_result(result, metadata["duration_seconds"])
                report.update({"status": status, "processed_audio_seconds": metadata["duration_seconds"],
                               "processing_complete": True, "processing_windows": windows,
                               "timeline_coverage": timeline_coverage(segments, metadata["duration_seconds"]),
                               "segments": segments, "raw_text": text, "warnings": warnings,
                               "output_directory": str(output)})
                write_outputs(output, text, report)
                print(json.dumps({key: value for key, value in report.items() if key not in ("raw_text", "segments")}, ensure_ascii=False, allow_nan=False))
                return 0 if status == "transcribed_unverified" else 3
            finally:
                # Close the mapping before deleting its backing file on Windows.
                if hasattr(audio, "_mmap"):
                    audio._mmap.close()
    except (TrialError, OSError, RuntimeError, ValueError, ImportError) as exc:
        report.update({"status": "failed", "error_code": getattr(exc, "code", "runtime_failure"), "error": str(exc)})
        print(json.dumps(report, ensure_ascii=False, allow_nan=False))
        return 2


if __name__ == "__main__":
    sys.exit(main())
