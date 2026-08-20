from ytmusicapi import YTMusic

from download.download import cycle_to_download


def extract_songs(playlist_id):
    ytmusic = YTMusic()
    playlist = ytmusic.get_playlist(playlist_id)

    download_list = []

    for track in playlist.get("tracks", []):
        track_title = track.get("title")
        artists = track.get("artists", [])
        track_artist = artists[0].get("name") if artists else None

        if track_title and track_artist:
            download_list.append({"name": track_title, "artist": track_artist})

    return download_list


def extract_youtube(playlist_id):
    songs = extract_songs(playlist_id)
    total = len(songs)
    failed = []

    cycle_to_download(failed, songs, total)
