import json
import time
from download.download import download_audio, cycle_to_download


def load_songs():
    with open("ytmusic_songs.json", "r", encoding="utf-8") as f:
        return json.load(f)


def download_songs():
    songs = load_songs()
    total = len(songs)
    failed = []

    print(f"\n{total} músicas para descarregar.\n")

    cycle_to_download(failed, songs, total)

    print(f"\nConcluído. {len(failed)} falharam:")
    for f in failed:
        print(f" - {f}")
