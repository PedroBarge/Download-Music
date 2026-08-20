from Enum_Support_Sources import SupportSource
from download.download import cycle_to_download
from extrat_playlist_embed import extract_playlist_embed


def extract_songs(playlist_id):
    url = f"https://open.spotify.com/embed/playlist/{playlist_id}?utm_source=generator"
    data = extract_playlist_embed(url, SupportSource.SPOTIFY)

    download_list = []

    entity = data.get("props").get("pageProps").get("state").get("data").get("entity")  # type:ignore
    track_list = entity.get("trackList")

    for track in track_list:
        track_title = track.get("title")
        track_artist = track.get("subtitle")
        download_list.append({"name": track_title, "artist": track_artist})

    return download_list


def extract_spotify(playlist_id):
    songs = extract_songs(playlist_id)
    total = len(songs)
    failed = []

    cycle_to_download(failed, songs, total)
