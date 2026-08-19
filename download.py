import subprocess
import shutil
import os

FFMPEG_PATH = os.environ.get("FFMPEG_PATH", "/home/barge/.config/spotdl/ffmpeg")


def download_audio(query, output_dir="downloads"):
    spotdl_path = shutil.which("spotdl")
    if not spotdl_path:
        spotdl_path = os.path.join(os.path.dirname(__file__), ".venv", "bin", "spotdl")

    os.makedirs(output_dir, exist_ok=True)

    result = subprocess.run([
        spotdl_path, "download", query,
        "--output", f"{output_dir}/{{artists}} - {{title}}.{{output-ext}}",
        "--archive", "archive.spotdl",
        "--ffmpeg", FFMPEG_PATH,
        "--yt-dlp-args", "--cookies-from-browser firefox",
        "--print-errors",
    ])

    return result.returncode == 0
