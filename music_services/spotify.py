import os
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth

from download import download_audio

SPOTIPY_CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID", "")
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET", "")
SPOTIPY_REDIRECT_URI = os.environ.get("SPOTIPY_REDIRECT_URI", "http://localhost:8888/callback")
SCOPE = "playlist-read-private playlist-read-collaborative user-library-read"


def _get_spotify_client():
    return spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope=SCOPE,
        cache_path=".spotify_cache",
    ))


def _get_playlist_tracks(sp, playlist_id):
    tracks = []
    results = sp.playlist_tracks(playlist_id)
    tracks.extend(results["items"])
    while results["next"]:
        results = sp.next(results)
        tracks.extend(results["items"])
    return tracks


def _get_liked_tracks(sp):
    tracks = []
    results = sp.current_user_saved_tracks()
    tracks.extend(results["items"])
    while results["next"]:
        results = sp.next(results)
        tracks.extend(results["items"])
    return tracks


def _print_playlists(sp):
    results = sp.current_user_playlists()
    playlists = results["items"]
    while results["next"]:
        results = sp.next(results)
        playlists.extend(results["items"])

    print("\nAs tuas playlists:")
    for i, pl in enumerate(playlists, 1):
        print(f"  {i}. {pl['name']} ({pl['tracks']['total']} músicas)")
    print(f"  L. Músicas Curtidas (Liked Songs)")

    return playlists


def spotify_request(playlist_url=None):
    sp = _get_spotify_client()
    user = sp.current_user()
    print(f"Autenticado como: {user['display_name']}")

    if playlist_url:
        playlist_id = playlist_url.split("/playlist/")[-1].split("?")[0]
        tracks = _get_playlist_tracks(sp, playlist_id)
        playlist_name = sp.playlist(playlist_id)["name"]
    else:
        playlists = _print_playlists(sp)
        choice = input("\nEscolhe o número da playlist (ou 'L' para Liked Songs): ").strip()

        if choice.upper() == "L":
            tracks = _get_liked_tracks(sp)
            playlist_name = "Liked Songs"
        else:
            idx = int(choice) - 1
            selected = playlists[idx]
            playlist_id = selected["id"]
            playlist_name = selected["name"]
            tracks = _get_playlist_tracks(sp, playlist_id)

    print(f"\nA descargar: {playlist_name} ({len(tracks)} músicas)")

    failed = []
    for i, item in enumerate(tracks, 1):
        track = item.get("track")
        if not track:
            continue
        name = track["name"]
        artists = ", ".join(a["name"] for a in track["artists"])
        query = f"{name} {artists}"

        print(f"[{i}/{len(tracks)}] {name} by {artists}")
        success = download_audio(query)
        if not success:
            failed.append(query)
        time.sleep(2)

    print(f"\nConcluído. {len(failed)} falharam:")
    for f in failed:
        print(f" - {f}")
