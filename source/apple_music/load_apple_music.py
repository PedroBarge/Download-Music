from source.apple_music.extract_apple_music_embed import extract_apple_music


def main():
    # user_response_name = input("Copy playlist Name: ")
    # user_response_id = input("Copy playlist ID: ")
    pl_name = "techno-rave" #  mock temporário
    pl_id = "mJy8gyJsNo1gy7y" #  mock temporário
    extract_apple_music(pl_name, pl_id)