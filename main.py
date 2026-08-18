from info import repo
from download import download_audio

def main():

    resources:dict = repo.get("resources")

    library_songs:dict = resources.get("library-songs")

    library_songs_keys = list(library_songs.keys())

    for key in library_songs_keys:
        id:dict = library_songs.get(key)
        attributes = id.get("attributes")
        albumName = attributes.get("albumName")
        artistName = attributes.get("artistName")
        name = attributes.get("name")
        print(f"{name} by {artistName}")

        query = f"{name} {artistName}"
        download_audio(query)


main()
