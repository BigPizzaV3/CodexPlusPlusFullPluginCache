---
name: metronome
description: Open a live metronome with tap tempo and tempo ramps, calculate BPM and note durations, or plan a tempo practice ladder with a CSV download.
---

# Beatwise Metronome

- Use `show_metronome` for a metronome, online metronome, tap tempo or bpm counter. Supply BPM (20–400), beats per bar, subdivision and accent pattern if requested. The first beat defaults to accented. An optional ramp starts at the given BPM, changes after complete bars and holds at target. Sound starts only after the user presses Start.
- Use `calculate_tempo_values` for bpm to ms, a delay time calculator, tempo calculator, note cycle hertz, reverse duration-to-BPM, bar length or song length. Supply BPM **or** milliseconds. For reverse conversion, pass the note value and modifier represented by the duration. For example, 250 ms straight eighth = 120 quarter-note BPM. BPM means quarter notes per minute; 6/8 changes bar length, not that convention. Hertz is repetition rate, not pitch. Italian marking ranges are approximate.
- Use `plan_tempo_practice` with start BPM, target BPM, a positive BPM or percent step, and minutes per stage. Up/down ladders include the target stage's time. Share the CSV download link, total time and preview. Up to 200 stages; percent steps round to 0.001 BPM.

If values are absent, use a 120 BPM metronome in 4/4 without subdivisions, or a practice ladder from 80 to 120 BPM in steps of 5 BPM with 2 minutes per stage; state the assumption. Inputs accept up to three decimal places.

The widget runs only while it is on the screen. Audio timing depends on the device. No recording, pitch detection or session tracking. Do not use these tools to analyze an uploaded recording or identify a song's tempo.
