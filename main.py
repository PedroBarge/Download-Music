import music_services.apple_music as apple_music
import music_services.spotify as spotify
import music_services.youtube as youtube


def main():
    print("=== Download Music ===\n")
    print("Escolhe a plataforma:")
    print("  1. Apple Music")
    print("  2. Spotify")
    print("  3. YouTube")
    print()

    choice = input("Opção: ").strip()

    if choice == "1":
        apple_music.apple_music_request()
    elif choice == "2":
        playlist_url = input("URL da playlist (ou Enter para ver as tuas playlists): ").strip()
        spotify.spotify_request(playlist_url or None)
    elif choice == "3":
        playlist_url = input("URL da playlist do YouTube: ").strip()
        youtube.youtube_request(playlist_url or None)
    else:
        print("Opção inválida.")


if __name__ == "__main__":
    main()
