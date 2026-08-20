from source.apple_music.extract_apple_music_embed import extract_apple_music


def main():
    # user_response_playlist_name = input("Copy playlist Name: ")
    # user_response_plalist_id = input("Copy playlist ID: ")
    user_response_playlist_name = "techno-rave" #  mock temporário
    user_response_plalist_id = "mJy8gyJsNo1gy7y" #  mock temporário
    extract_apple_music(user_response_playlist_name, user_response_plalist_id)