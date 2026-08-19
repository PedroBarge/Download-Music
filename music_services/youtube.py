import json
import subprocess
import shutil
import os
import re
import time


def _get_ytdlp_path():
    path = shutil.which("yt-dlp")
    if not path:
        path = os.path.join(os.path.dirname(__file__), "..", ".venv", "bin", "yt-dlp")
    return path


def _extract_playlist_info(playlist_url):
    ytdlp = _get_ytdlp_path()
    result = subprocess.run(
        [ytdlp, "--flat-playlist", "--dump-json", playlist_url],
        capture_output=True, text=True
    )
    videos = []
    for line in result.stdout.strip().split("\n"):
        if line:
            videos.append(json.loads(line))
    return videos


def _parse_title(title):
    # Common YouTube title formats:
    # "Artist - Title (Official Video)"
    # "Artist - Title [Official Music Video]"
    # "Title - Artist"
    # Just "Title"
    clean = re.sub(r"\(.*?\)|\[.*?\]|Official.*|Music Video|Audio|HD|4K|Lyrics", "", title, flags=re.IGNORECASE)
    clean = clean.strip(" -–")

    if " - " in clean:
        parts = clean.split(" - ", 1)
        # Heuristic: if first part looks like an artist (shorter), treat as artist
        if len(parts[0]) < len(parts[1]):
            return f"{parts[1].strip()} {parts[0].strip()}"
        return f"{parts[0].strip()} {parts[1].strip()}"

    # Fallback: use the whole title as query
    return clean


def youtube_request(playlist_url=None):
    if not playlist_url:
        playlist_url = input("URL da playlist do YouTube: ").strip()

    if not playlist_url:
        print("URL inválida.")
        return

    print(f"A extrair informações da playlist...")
    videos = _extract_playlist_info(playlist_url)

    if not videos:
        print("Não foi possível extrair vídeos da playlist.")
        return

    print(f"Encontrados {len(videos)} vídeos. A iniciar download...\n")

    from download import download_audio

    failed = []
    for i, video in enumerate(videos, 1):
        title = video.get("title", "Unknown")
        query = _parse_title(title)

        print(f"[{i}/{len(videos)}] {title}")
        print(f"    Query: {query}")

        success = download_audio(query)
        if not success:
            failed.append(query)
        time.sleep(2)

    print(f"\nConcluído. {len(failed)} falharam:")
    for f in failed:
        print(f" - {f}")
