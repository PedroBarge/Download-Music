# Download-Music

A Python CLI tool that extracts song listings from streaming service playlists (Spotify, Apple Music) and batch-downloads the audio locally using [spotdl](https://github.com/spotdl/spotify-downloader).

## Features

- **Spotify** and **Apple Music** playlist support
- Scrapes public embed pages to extract track listings (no API keys needed)
- Batch downloads all tracks with duplicate avoidance via archive tracking
- Browser cookie integration for age-restricted / region-locked content

## Requirements

- Python 3.13+
- [ffmpeg](https://ffmpeg.org/) (installed at `~/.config/spotdl/ffmpeg` or adjust the path in `download/download.py`)
- Firefox browser (for cookie-based YouTube access)

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

Select a source when prompted:

| Option | Source       | Status        |
|--------|-------------|---------------|
| 1      | Apple Music | Working       |
| 2      | Spotify     | Working       |
| 3      | YouTube Music | Incomplete  |

Downloaded files are saved to the `downloads/` directory.

## Project Structure

```
Download-Music/
├── main.py                         # Entry point & CLI menu
├── Enum_Support_Sources.py         # Supported source enum
├── extrat_playlist_embed.py        # Embed page scraper
├── requirements.txt                # Python dependencies
├── download/
│   └── download.py                 # spotdl download wrapper
├── source/
│   ├── spotify/
│   │   ├── load_spotify.py         # Spotify playlist loader
│   │   └── extract_spotify_embed.py
│   ├── apple_music/
│   │   ├── load_apple_music.py     # Apple Music playlist loader
│   │   └── extract_apple_music_embed.py
│   └── youtube/
│       └── ytmusic.py              # YouTube Music (WIP)
└── downloads/                      # Output directory
```

## Dependencies

| Package     | Purpose                              |
|-------------|--------------------------------------|
| `spotdl`    | Audio downloader (wraps yt-dlp + ffmpeg) |
| `requests`  | HTTP requests for embed page scraping|

## Notes

- Playlist IDs are currently hardcoded in `load_spotify.py` and `load_apple_music.py`. Uncomment the `input()` calls to enable user prompts.
- The ffmpeg path in `download/download.py` is hardcoded and may need adjustment for your system.
- YouTube Music support is still a work in progress.
