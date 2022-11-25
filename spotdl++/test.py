from cgitb import text
import sys
from pathlib import Path
sys.path.append(str(Path.cwd()))

from spotdl import Spotdl
from spotdl.utils.config import DEFAULT_CONFIG
from spotdl.types.song import Song
from spotdl.utils.spotify import SpotifyClient
from spotdl.utils.search import get_simple_songs
import requests
import json
from spotdl.utils.search import reinit_song

def main():
    spotdl = Spotdl(
        client_id=DEFAULT_CONFIG["client_id"],
        client_secret=DEFAULT_CONFIG["client_secret"],
        user_auth=DEFAULT_CONFIG["user_auth"],
        cache_path=DEFAULT_CONFIG["cache_path"],
        no_cache=True,
        headless=DEFAULT_CONFIG["headless"],
        audio_providers=["youtube"],
        lyrics_providers=DEFAULT_CONFIG["lyrics_providers"],
        ffmpeg=DEFAULT_CONFIG["ffmpeg"],
        bitrate=DEFAULT_CONFIG["bitrate"],
        ffmpeg_args=DEFAULT_CONFIG["ffmpeg_args"],
        output_format=DEFAULT_CONFIG["format"],
        threads=DEFAULT_CONFIG["threads"],
        output=str(Path.cwd()),
        save_file=DEFAULT_CONFIG["save_file"],
        overwrite=DEFAULT_CONFIG["overwrite"],
        cookie_file=DEFAULT_CONFIG["cookie_file"],
        filter_results=DEFAULT_CONFIG["filter_results"],
        search_query=DEFAULT_CONFIG["search_query"],
        log_level="DEBUG",
        simple_tui=True,
        restrict=DEFAULT_CONFIG["restrict"],
        print_errors=DEFAULT_CONFIG["print_errors"],
    )

    # song = {
    #     "name": "Nobody Else",
    #     "artists": ["Abstrakt"],
    #     "artist": "Abstrakt",
    #     "album_name": "Nobody Else",
    #     "album_artist": "Abstrakt",
    #     "genres": [],
    #     "disc_number": 1,
    #     "disc_count": 1,
    #     "duration": 162.406,
    #     "year": 2022,
    #     "date": "2022-03-17",
    #     "track_number": 1,
    #     "tracks_count": 1,
    #     "isrc": "GB2LD2210007",
    #     "song_id": "0kx3ml8bdAYrQtcIwvkhp8",
    #     "cover_url": "https://i.scdn.co/image/ab67616d0000b27345f5ba253b9825efc88bc236",
    #     "explicit": False,
    #     "publisher": "NCS",
    #     "url": "https://open.spotify.com/track/0kx3ml8bdAYrQtcIwvkhp8",
    #     "copyright_text": "2022 NCS",
    #     "download_url": "https://www.youtube.com/watch?v=nfyk-V5CoIE",
    #     "song_list": None,
    # }
    input_url = "https://open.spotify.com/playlist/1SdVVqpwdD5WjSWTpdGs68?si=542f1cfbdd984a90"
    # input_url = input("URL:")
    songs = []
    for song in get_simple_songs([input_url]):
        songs.append(reinit_song(song))

    for song in songs:
        print(song.name)
    download_urls = []
    aps = []
    for song in songs:
        try:
            doownload_url, audio_provider = spotdl.downloader.search(song)
            download_urls.append(doownload_url)
            aps.append(audio_provider)
        except LookupError:
            download_urls.append(None)
            aps.append(None)
    print(download_urls)
    print(aps)
    
    # spotdl.download_songs(songs)
    
if __name__ == '__main__':
    main()
    pass