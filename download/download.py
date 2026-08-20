import subprocess
import shutil
import os
import time
from typing import Any


def cycle_to_download(failed: list[Any], songs: list[Any], total: int):
    for i, song in enumerate(songs, 1):
        query = f"{song['name']} {song['artist']}"
        print(f"[{i}/{total}] {song['name']} by {song['artist']}")

        success = download_audio(query)
        if not success:
            failed.append(query)

        time.sleep(2)


def download_audio(query, output_dir="downloads"):
    spotdl_path = shutil.which("spotdl")
    if not spotdl_path:
        spotdl_path = os.path.join(os.path.dirname(__file__), ".venv", "bin", "spotdl")

    os.makedirs(output_dir, exist_ok=True)

    result = subprocess.run([
        spotdl_path, "download", query,
        "--output", f"{output_dir}/{{artists}} - {{title}}.{{output-ext}}",
        "--archive", "archive.spotdl",
        "--ffmpeg", "/home/barge/.config/spotdl/ffmpeg",
        "--yt-dlp-args", "--cookies-from-browser firefox",
        "--print-errors",
    ])

    return result.returncode == 0
