import time

from download import download_audio
from info import repo


def apple_music_request():
    resources = repo.get("resources")
    library_songs = resources.get("library-songs")
    library_songs_keys = library_songs.keys()

    failed = []
    total = len(list(library_songs_keys))

    for i, key in enumerate(library_songs.keys(), 1):
        song = library_songs.get(key)
        attributes = song.get("attributes")
        artist_name = attributes.get("artistName")
        name = attributes.get("name")
        query = f"{name} {artist_name}"

        print(f"[{i}/{total}] {name} by {artist_name}")

        success = download_audio(query)
        if not success:
            failed.append(query)

        time.sleep(2)

    print(f"\nConcluído. {len(failed)} falharam:")
    for f in failed:
        print(f" - {f}")
