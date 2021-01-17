import sys

import pytest

from moviecreator.create_movie import parse_arguments


def test_mandatory_arguments():

    sys.argv = ["create_movie"]
    with pytest.raises(SystemExit):
        _ = parse_arguments()

    sys.argv = ["create_movie", "--video-name", "x.mp4"]
    with pytest.raises(SystemExit):
        _ = parse_arguments()

    sys.argv = ["create_movie", "--video-name", "x.mp4", "--files", "*.png"]
    args = parse_arguments()
    assert args.files == "*.png"
    assert args.video_name == "x.mp4"


def test_verbose():

    sys.argv = ["", "--verbose", "--video-name", "x.mp4", "--files", "*.png"]
    args = parse_arguments()
    assert args.verbose == 1

    sys.argv = ["", "--verbose", "--video-name", "x.mp4", "--files", "*.png", "--verbose"]
    args = parse_arguments()
    assert args.verbose == 2

    sys.argv = ["", "-v", "--video-name", "x.mp4", "--files", "*.png"]
    args = parse_arguments()
    assert args.verbose == 1

    sys.argv = ["", "-vvv", "--video-name", "x.mp4", "--files", "*.png"]
    args = parse_arguments()
    assert args.verbose == 3


def test_shape():

    # This test will print a usage and error message on the screen, that is expected

    sys.argv = ["", "--video-name", "x.mp4", "--files", "*.png", "--shape", "1000, 1000, 4"]
    with pytest.raises(SystemExit):
        _ = parse_arguments()

    sys.argv = ["", "--video-name", "x.mp4", "--files", "*.png", "--shape", "(1000, 1000)"]
    args = parse_arguments()
    assert args.shape == (1000, 1000)

    sys.argv = ["", "--video-name", "x.mp4", "--files", "*.png", "--shape", "(1000, 1000, 4)"]
    args = parse_arguments()
    assert args.shape == (1000, 1000, 4)
