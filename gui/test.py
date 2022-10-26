import os
import sys
o_path = os.getcwd()
sys.path.append(o_path)
from spotdl import Spotdl
from spotdl.utils.config import DEFAULT_CONFIG
from spotdl.types.song import Song


# 得到当前根目录


def main():
    spotdl = Spotdl(
        client_id=DEFAULT_CONFIG["client_id"],
        client_secret=DEFAULT_CONFIG["client_secret"],
        user_auth=DEFAULT_CONFIG["user_auth"],
        cache_path=DEFAULT_CONFIG["cache_path"],
        no_cache=True,
        headless=DEFAULT_CONFIG["headless"],
        audio_providers=DEFAULT_CONFIG["audio_providers"],
        lyrics_providers=DEFAULT_CONFIG["lyrics_providers"],
        ffmpeg=DEFAULT_CONFIG["ffmpeg"],
        bitrate=DEFAULT_CONFIG["bitrate"],
        ffmpeg_args=DEFAULT_CONFIG["ffmpeg_args"],
        output_format=DEFAULT_CONFIG["format"],
        threads=DEFAULT_CONFIG["threads"],
        output=DEFAULT_CONFIG["output"],
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
    # From Spotify URL to download URL
    # urls = spotdl.get_download_urls(
    #     [Song.from_url("https://open.spotify.com/track/0kx3ml8bdAYrQtcIwvkhp8")]
    # )
    # print(urls)
    songs = spotdl.search(["装帧"])
    urls = spotdl.get_download_urls(songs)
    print(urls)

if __name__ == '__main__':
    main()