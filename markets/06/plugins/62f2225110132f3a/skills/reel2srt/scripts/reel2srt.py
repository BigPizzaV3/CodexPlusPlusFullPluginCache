#!/usr/bin/env python3
"""Reel2SRT: local audio -> word timings -> strictly bounded UTF-8 SRT."""
import argparse
import json
import math
import unicodedata
from pathlib import Path

class QualityError(ValueError):
    pass

def number(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise QualityError('Expected finite numeric timestamp')
    return value

def build_cues(words, duration):
    number(duration)
    if not 0 < duration <= 300:
        raise QualityError('Video duration must be > 0 and <= 300 seconds')
    normalized, previous = [], 0.0
    for raw in words:
        start, end = number(raw['start']), number(raw['end'])
        text = raw['word']
        if not isinstance(text, str) or not text.strip() or '\n' in text or '\r' in text or '-->' in text:
            raise QualityError('Invalid word text; review alignment')
        if not 0 <= start <= end <= duration or start < previous - 1e-9:
            raise QualityError('Invalid, overlapping, or out-of-bounds word; re-align, never stretch')
        joins_grapheme = unicodedata.category(text.lstrip()[0]).startswith('M') or (normalized and normalized[-1]['word'][-1] in 'เแโใไ')
        if joins_grapheme:
            if not normalized or start - normalized[-1]['end'] >= .20 - 1e-9:
                raise QualityError('Detached Thai combining character; review alignment')
            normalized[-1]['word'] += text
            normalized[-1]['end'] = end
        else:
            normalized.append(dict(raw))
        previous = end
    cues, group = [], []
    for raw in normalized:
        start, end, text = raw['start'], raw['end'], raw['word']
        if group and (start - group[-1]['end'] >= .20 - 1e-9 or
                      len(''.join(w['word'] for w in group) + text) > 42 or
                      end - group[0]['start'] > 4.5):
            cues.append(group)
            group = []
        group.append(raw)
        previous = end
    if group:
        cues.append(group)
    result = []
    for group in cues:
        # Round inward: exported timestamps never precede/follow measured words.
        start = math.ceil(group[0]['start'] * 1000 - 1e-7)
        end = math.floor(group[-1]['end'] * 1000 + 1e-7)
        if start >= end:
            raise QualityError('Cue has no positive millisecond interval; review alignment')
        text = ''.join(w['word'] for w in group).strip()
        if len(text) > 42 or end - start > 4500:
            raise QualityError('Single word exceeds cue limit; review audio, do not invent split timing')
        result.append({'start_ms': start, 'end_ms': end, 'text': text})
    return result

def timestamp(ms):
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f'{h:02d}:{m:02d}:{s:02d},{ms:03d}'

def render(cues):
    return ''.join(f"{i}\n{timestamp(c['start_ms'])} --> {timestamp(c['end_ms'])}\n{c['text']}\n\n"
                   for i, c in enumerate(cues, 1))

def decode_timeline(path):
    import av
    import numpy as np
    with av.open(str(path)) as container:
        if not container.streams.video:
            raise QualityError('Expected a video file')
        if len(container.streams.audio) != 1:
            raise QualityError('Expected exactly one audio track; select/export the intended track first')
        if container.duration is None:
            raise QualityError('Unknown duration; cannot enforce 5-minute limit')
        duration = float(container.duration / av.time_base)
        build_cues([], duration)
        origin = float((container.start_time or 0) / av.time_base)
        audio = np.zeros(math.ceil(duration * 16000), dtype=np.float32)
        resampler = av.AudioResampler(format='fltp', layout='mono', rate=16000)
        last_end = 0
        decoded = False
        def place(frame):
            nonlocal last_end, decoded
            if frame.pts is None:
                raise QualityError('Audio timestamps missing; cannot preserve video alignment')
            start = round((float(frame.pts * frame.time_base) - origin) * 16000)
            samples = frame.to_ndarray().reshape(-1)
            end = start + len(samples)
            if start < last_end - 1 and decoded:
                raise QualityError('Overlapping audio frame timestamps')
            left, right = max(0, start), min(len(audio), end)
            if right > left:
                audio[left:right] = samples[left-start:right-start]
                decoded = True
            last_end = end
        for frame in container.decode(audio=0):
            for converted in resampler.resample(frame):
                place(converted)
        for converted in resampler.resample(None):
            place(converted)
        if not decoded:
            raise QualityError('Audio track could not be decoded')
    return audio, duration

def transcribe(path, language, model_path, allow_download=False):
    import faster_whisper
    from faster_whisper import WhisperModel
    audio, duration = decode_timeline(path)
    model = WhisperModel(model_path, device='cpu', compute_type='int8',
                         local_files_only=not allow_download)
    segments, info = model.transcribe(audio, language=None if language == 'auto' else language,
        task='transcribe', beam_size=5, vad_filter=True,
        vad_parameters={'min_silence_duration_ms': 200}, word_timestamps=True,
        condition_on_previous_text=False, temperature=0.0)
    words = []
    for segment in segments:
        if segment.text.strip() and not segment.words:
            raise QualityError('Recognizer returned text without word timestamps')
        for w in segment.words or []:
            if w.word.strip():
                words.append({'word': w.word, 'start': float(w.start), 'end': float(w.end),
                              'probability': float(w.probability)})
    return {'duration': duration, 'language': info.language,
            'language_probability': info.language_probability, 'words': words,
            'engine': 'faster-whisper', 'engine_version': faster_whisper.__version__,
            'model': model_path, 'timing_source': 'decoded audio on original video timeline'}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument('--video', type=Path)
    source.add_argument('--alignment', type=Path, help='Replay only: trusted word timings JSON, not new transcription')
    parser.add_argument('--out', required=True, type=Path)
    parser.add_argument('--language', choices=['auto', 'th', 'en'], default='auto')
    parser.add_argument('--model', default='large-v3-turbo')
    parser.add_argument('--allow-model-download', action='store_true')
    args = parser.parse_args()
    report_path = args.out.with_suffix('.report.json')
    alignment_path = args.out.with_suffix('.alignment.json')
    if args.out.suffix.lower() != '.srt':
        parser.error('--out must end with .srt')
    if any(p.exists() for p in (args.out, report_path, alignment_path)):
        parser.error('Output exists; choose a fresh filename to preserve prior results')
    args.out.parent.mkdir(parents=True, exist_ok=True)
    try:
        data = (json.loads(args.alignment.read_text(encoding='utf-8')) if args.alignment else
                transcribe(args.video, args.language, args.model, args.allow_model_download))
        if 'words' not in data and 'segments' in data:
            data['words'] = [w for s in data['segments'] for w in s.get('words', [])]
        alignment_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
        cues = build_cues(data['words'], data['duration'])
        uncertain = [i for i, w in enumerate(data['words']) if w.get('probability', 1) < .5]
        report = {'status': 'draft_needs_audio_review' if cues else 'no_speech_detected',
                  'mode': 'alignment_replay' if args.alignment else 'video_transcription',
                  'duration': data['duration'], 'cues': len(cues),
                  'low_confidence_word_indices': uncertain,
                  'structural_checks': 'passed', 'human_audio_review': 'pending',
                  'capcut_import': 'pending',
                  'note': 'Structural validity does not establish recognition or acoustic timing accuracy.'}
        if cues:
            args.out.write_text(render(cues), encoding='utf-8')
        report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
        print(json.dumps(report, ensure_ascii=False))
    except (QualityError, KeyError, TypeError, ValueError, ImportError, OSError, RuntimeError) as error:
        report_path.write_text(json.dumps({'status':'blocked', 'reason':str(error)}, ensure_ascii=False, indent=2), encoding='utf-8')
        parser.exit(2, f'Reel2SRT blocked: {error}\n')

if __name__ == '__main__':
    main()
