
from source.spotify.extract_spotify_embed import extract_spotify


def main():
    # user_response = input("Copy playlist ID: ")
    user_response = "5DutDksCDPMirP40odZ0gf" # mock temporário
    extract_spotify(user_response)