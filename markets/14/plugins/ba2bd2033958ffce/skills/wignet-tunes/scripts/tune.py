#!/usr/bin/env python3
"""Check an MML v1 alarm tune and preview it, before handing it to the frame.

    python3 tune.py check wake.mml        # verdict, beats per line, normalized text
    python3 tune.py wav wake.mml -o wake.wav [--loops 2] [--rate 32000]
    python3 tune.py link wake.mml --base <platform origin>   # browser player link
    echo "A t120 o5 l8 c e g" | python3 tune.py check -

`check` uses the platform's own parser (mml.py, next to this file), so a tune
that passes here is accepted by update_alarm. Its beats-per-line table is the
quick way to fix the usual mistake, channels of different lengths.

`wav` renders what the frame's synthesizer plays, sample for sample at the
same rate (tests compare it with the firmware build), so the owner can listen
before the alarm rings. `link` prints the platform's player link for the
tune (the tune rides in the link itself), which plays it in any browser.
Standard library only.
"""
import argparse
import base64
import os
import sys
import wave

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    import mml
except ImportError:  # run from the repository, before the skill is built
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    "..", "..", "..", ".."))
    from backoffice import mml

FRAME_RATE = 48000
CHANNEL_SPAN = 16000  # peak to peak at v15, as in mml_tune.cpp
_DUTY_EIGHTHS = (1, 2, 4, 6)


def _tdiv(a, b):
    """C integer division, which truncates toward zero."""
    q = abs(a) // b
    return q if a >= 0 else -q


def render(tune, rate=FRAME_RATE, loops=1):
    """Mono int16 samples of `loops` passes, mirroring Mml::Synth::render."""
    loop_samples = tune.length_ticks * rate * 60 // (tune.tempo * mml.TICKS_PER_QUARTER)

    def sample_at(tick):
        return tick * rate * 60 // (tune.tempo * mml.TICKS_PER_QUARTER)

    out = []
    for _ in range(loops):
        voices = []
        for index, channel in enumerate(mml.CHANNELS):
            notes = tune.channels.get(channel)
            if notes is None:
                continue
            voices.append({"index": index, "notes": iter(notes), "note": None, "end": 0,
                           "gate_end": 0, "phase": 0, "inc": 0, "lfsr": 0, "level": 0,
                           "env": 0, "done": False})
        for sample in range(loop_samples):
            mix = 0
            for v in voices:
                while not v["done"] and sample >= v["end"]:
                    note = next(v["notes"], None)
                    if note is None:
                        v["done"], v["note"] = True, None
                        break
                    v["note"] = note
                    v["gate_end"] = sample_at(note.tick + note.gate)
                    v["end"] = sample_at(note.tick + note.length)
                    if note.note < 0:
                        continue
                    frequency = 440.0 * pow(2.0, (note.note - 69) / 12.0)
                    if v["index"] == 3:
                        frequency = min(frequency * 8.0, rate * 0.99)
                    v["inc"] = int(frequency * 4294967296.0 / rate)
                    v["phase"], v["lfsr"], v["level"], v["env"] = 0, 0x7FFF, note.volume, 0
                note = v["note"]
                if v["done"] or note is None or note.note < 0 or sample >= v["gate_end"]:
                    continue
                if note.envelope and v["level"]:
                    v["env"] += 1
                    if v["env"] >= note.envelope * rate // 64:
                        v["env"] = 0
                        v["level"] -= 1
                index, phase = v["index"], v["phase"]
                if index < 2:
                    duty = _DUTY_EIGHTHS[note.timbre]
                    value = (CHANNEL_SPAN * (8 - duty) // 8 if phase < (duty << 29)
                             else -(CHANNEL_SPAN * duty // 8))
                elif index == 2:
                    t = phase >> 16
                    if note.timbre == 0:
                        value = _tdiv((t - 16384 if t < 32768 else 49151 - t) * CHANNEL_SPAN, 32768)
                    else:
                        value = _tdiv((t - 32768) * CHANNEL_SPAN, 65536)
                else:
                    value = -CHANNEL_SPAN // 2 if v["lfsr"] & 1 else CHANNEL_SPAN // 2
                v["phase"] = (phase + v["inc"]) & 0xFFFFFFFF
                if index == 3 and v["phase"] < phase:
                    lfsr = v["lfsr"]
                    bit = (lfsr ^ (lfsr >> 1)) & 1
                    lfsr = (lfsr >> 1) | (bit << 14)
                    if note.timbre == 1:
                        lfsr = (lfsr & ~(1 << 6)) | (bit << 6)
                    v["lfsr"] = lfsr & 0xFFFF
                mix += _tdiv(value * v["level"], 15)
            out.append(max(-32768, min(32767, mix)))
    return out


def _beats(ticks):
    return f"{ticks / mml.TICKS_PER_QUARTER:g}"


def beat_table(text):
    """[(input line, channel, beats)] and {channel: total ticks}, as far as it parses."""
    lines = mml._split(text)
    rows, totals = {}, {}
    for channel in mml.CHANNELS:
        if not any(ch == channel for _, ch, _ in lines):
            continue
        cursor = mml._Cursor(lines, channel)
        try:
            for note in cursor.notes():
                rows[note.line] = rows.get(note.line, 0) + note.length
        except mml.MmlError:
            pass  # the verdict reports it; show what parsed
        totals[channel] = cursor.tick
    table = [(number, ch, rows.get(number, 0)) for number, ch, _ in lines]
    return table, totals


def check(text):
    try:
        tune = mml.parse(text)
        verdict, ok = None, True
    except mml.MmlError as exc:
        tune, verdict, ok = None, str(exc), False
    if ok:
        print(f"OK: {tune.seconds:.1f} s per loop at t{tune.tempo}, "
              f"channels {''.join(tune.channels)}, {len(tune.text.encode())} bytes normalized "
              f"(limit {mml.MAX_BYTES})")
    else:
        print(f"ERROR {verdict}")
    try:
        table, totals = beat_table(text)
    except mml.MmlError:
        return ok
    print("\nBeats per line (the lines of each channel add up; every channel "
          "must reach the same total):")
    for number, channel, ticks in table:
        print(f"  line {number:>3}  {channel}  {_beats(ticks):>6}")
    print("Totals: " + "  ".join(f"{ch} {_beats(t)}" for ch, t in totals.items()))
    if ok:
        print("\nNormalized (what the frame receives):\n" + tune.text)
    return ok


def write_wav(tune, path, rate, loops):
    samples = render(tune, rate=rate, loops=loops)
    with wave.open(path, "wb") as out:
        out.setnchannels(1)
        out.setsampwidth(2)
        out.setframerate(rate)
        out.writeframes(b"".join(int(s).to_bytes(2, "little", signed=True) for s in samples))
    return len(samples)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("check", "wav", "link"):
        cmd = sub.add_parser(name)
        cmd.add_argument("file", help="tune file, or - for standard input")
        if name == "link":
            cmd.add_argument("--base", required=True,
                             help="the platform origin, as SKILL.md gives it")
        if name == "wav":
            cmd.add_argument("-o", "--output", required=True)
            cmd.add_argument("--loops", type=int, default=2)
            cmd.add_argument("--rate", type=int, default=FRAME_RATE,
                             help="48000 is the frame's rate; lower renders faster")
    args = parser.parse_args(argv)
    if args.file == "-":
        text = sys.stdin.read()
    else:
        with open(args.file, encoding="utf-8") as handle:
            text = handle.read()
    if args.command == "check":
        return 0 if check(text) else 1
    try:
        tune = mml.parse(text)
    except mml.MmlError as exc:
        print(f"ERROR {exc}")
        return 1
    if args.command == "link":
        # Same encoding as the platform's preview_tune: base64url, unpadded.
        fragment = base64.urlsafe_b64encode(tune.text.encode("utf-8")).decode("ascii").rstrip("=")
        print(f"{args.base.rstrip('/')}/w/tune#{fragment}")
        return 0
    count = write_wav(tune, args.output, args.rate, max(1, args.loops))
    print(f"{args.output}: {count / args.rate:.1f} s, {args.rate} Hz mono. The frame "
          "also fades it in over the alarm's fade_in_seconds.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
