from Enum_Support_Sources import SupportSource
from download.download import cycle_to_download
from extrat_playlist_embed import extract_playlist_embed


def extract_songs(playlist_name, playlist_id):
    url = f"https://music.apple.com/pt/playlist/{playlist_name}/pl.u-{playlist_id}"
    response = extract_playlist_embed(url, SupportSource.APPLE_MUSIC)

    download_list = []

    data = response.get("data")[-1].get("data")
    sections = data.get("sections")
    playlist_items = sections[1].get("items")

    for item in playlist_items:
        if "track-lockup" in item.get("id"):
            track_title = item.get("title")
            track_artist = item.get("artistName")
            download_list.append({"name": track_title, "artist": track_artist})

    return download_list


def extract_apple_music(playlist_name, playlist_id):
    songs = extract_songs(playlist_name, playlist_id)
    total = len(songs)
    failed = []

    cycle_to_download(failed, songs, total)
