#!/bin/sh
set -eu

usage() {
  echo "Usage: $0 INPUT_VIDEO OUTPUT_DIR [INTERVAL_SECONDS]" >&2
}

if [ "${1:-}" = "--help" ] || [ "${1:-}" = "-h" ]; then
  usage
  exit 0
fi

if [ "$#" -lt 2 ] || [ "$#" -gt 3 ]; then
  usage
  exit 2
fi

input_video=$1
output_dir=$2
interval_seconds=${3-5}

if [ ! -f "$input_video" ]; then
  echo "Input video not found: $input_video" >&2
  exit 3
fi

if ! printf '%s\n' "$interval_seconds" | LC_ALL=C awk '
  /^[0-9]+([.][0-9]+)?$/ {
    value = $0 + 0
    if (value > 0 && tolower(sprintf("%g", value)) !~ /inf|nan/) valid = 1
  }
  END { exit !(NR == 1 && valid) }
'; then
  echo "Interval must be a positive number." >&2
  exit 4
fi

if ! command -v ffmpeg >/dev/null 2>&1 || ! command -v ffprobe >/dev/null 2>&1; then
  echo "ffmpeg and ffprobe are required but were not found." >&2
  exit 5
fi

mkdir -p "$output_dir/frames-interval" "$output_dir/frames-scenes"

ffprobe -v error -show_format -show_streams -of json "$input_video" > "$output_dir/metadata.json"
audio_stream=$(ffprobe -v error -select_streams a:0 -show_entries stream=index -of csv=p=0 "$input_video")
audio_status=ABSENT
audio_path=
if [ -n "$audio_stream" ]; then
  ffmpeg -nostdin -hide_banner -loglevel error -i "$input_video" -map 0:a:0 -ac 1 -ar 16000 -c:a pcm_s16le "$output_dir/audio-analysis.wav"
  audio_status=PRESENT
  audio_path=$output_dir/audio-analysis.wav
fi
ffmpeg -nostdin -hide_banner -loglevel error -i "$input_video" -vf "fps=1/$interval_seconds:round=up,scale='min(1280,iw)':-2" -pix_fmt yuvj420p -q:v 2 "$output_dir/frames-interval/frame-%06d.jpg"
ffmpeg -nostdin -hide_banner -loglevel error -i "$input_video" -vf "select='gt(scene,0.30)',scale='min(1280,iw)':-2,showinfo" -fps_mode vfr -pix_fmt yuvj420p -q:v 2 "$output_dir/frames-scenes/scene-%06d.jpg" 2> "$output_dir/scene-log.txt"

{
  echo "source=$input_video"
  echo "interval_seconds=$interval_seconds"
  echo "metadata=$output_dir/metadata.json"
  echo "audio_status=$audio_status"
  echo "audio=$audio_path"
  echo "interval_frames=$output_dir/frames-interval"
  echo "scene_frames=$output_dir/frames-scenes"
  echo "scene_log=$output_dir/scene-log.txt"
} > "$output_dir/manifest.txt"

echo "$output_dir/manifest.txt"
