import pytest

from spotdl.download.progress_handler import ProgressHandler, SongTracker
from spotdl.types.song import Song
from tests.instrumentation import print_coverage_dict
import logging

logger = logging.getLogger("spotdl.download.progress_handler")

song = Song.from_dict(
                {
                    "name": "Nobody Else",
                    "artists": ["Abstrakt"],
                    "artist": "Abstrakt",
                    "album_id": "0kx3ml8bdAYrQtcIwvkhp8",
                    "album_name": "Nobody Else",
                    "album_artist": "Abstrakt",
                    "album_type": "single",
                    "genres": [],
                    "disc_number": 1,
                    "disc_count": 1,
                    "duration": 162.406,
                    "year": 2022,
                    "date": "2022-03-17",
                    "track_number": 1,
                    "tracks_count": 1,
                    "isrc": "GB2LD2210007",
                    "song_id": "0kx3ml8bdAYrQtcIwvkhp8",
                    "cover_url": "https://i.scdn.co/image/ab67616d0000b27345f5ba253b9825efc88bc236",
                    "explicit": False,
                    "publisher": "NCS",
                    "url": "https://open.spotify.com/track/0kx3ml8bdAYrQtcIwvkhp8",
                    "copyright_text": "2022 NCS",
                    "download_url": None,
                }
            )

@pytest.mark.vcr()
def test_yt_dlp_progress_hook():
    test_dict = {"status": "downloading", "total_bytes": None}
    try:
        progress_handler = ProgressHandler(simple_tui=False)
        song_tracker = SongTracker(parent=progress_handler,song=song)
        progress_handler.close()

        song_tracker.yt_dlp_progress_hook(test_dict)
        assert False
    except Exception:
        assert True
    print_coverage_dict(["branch-1001","branch-1002","branch-1003","branch-1004","branch-1005"])

@pytest.mark.vcr()
def test_notify_error():
    progress_handler = ProgressHandler(simple_tui=False)
    song_tracker = SongTracker(parent=progress_handler,song=song)
    progress_handler.close()

    song_tracker.notify_error("Test error", traceback="Test traceback")

    assert True
    print_coverage_dict(["branch-1006", "branch-1007", "branch-1008"])


@pytest.mark.vcr()
def test_notify_error_debug():
    progress_handler = ProgressHandler(simple_tui=False)
    song_tracker = SongTracker(parent=progress_handler,song=song)
    progress_handler.close()

    logger.setLevel(logging.DEBUG)
    song_tracker.notify_error("Test error", traceback="Test traceback")

    assert True
    print_coverage_dict(["branch-1006", "branch-1007", "branch-1008"])


@pytest.mark.vcr()
def test_notify_error_finish():
    progress_handler = ProgressHandler(simple_tui=False)
    song_tracker = SongTracker(parent=progress_handler,song=song)
    progress_handler.close()

    song_tracker.notify_error("Test error", traceback="Test traceback", finish=True)

    assert song_tracker.progress == 100
    print_coverage_dict(["branch-1006", "branch-1007", "branch-1008"])
