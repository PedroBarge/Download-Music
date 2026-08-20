from source.apple_music import load_apple_music
from source.spotify import load_spotify


def main():
    print("Supported sources:")
    print("1. Apple Music")
    print("2. Spotify")
    print("3. YouTube Music")

    user_response = input("->")
    if user_response == "1":
        load_apple_music.main()
        return
    elif user_response == "2":
        load_spotify.main()
        return
    elif user_response == "3":

        return
    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()
