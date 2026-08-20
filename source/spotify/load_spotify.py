
from source.spotify.extract_spotify_embed import extract_spotify


def main():
    # user_response_playlist_id = input("Copy playlist ID: ")
    user_response_playlist_id = "5DutDksCDPMirP40odZ0gf" # mock temporário
    extract_spotify(user_response_playlist_id)