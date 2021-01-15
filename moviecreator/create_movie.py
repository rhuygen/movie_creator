"""Create a movie from a list of images."""
import imageio
import glob
import argparse
from skimage.transform import resize
from skimage.util import img_as_ubyte

from rich.console import Console


def create_movie(video_name, video_format, fn_glob, *, shape, loop, noresize):
    """
    Create an MP4 movie from the PNG images

    All images need to be the same size. Therefore they will be resized. If the
    shape argument is not given, all images will be resized to the shape of the first image.
    Please note the image shape is a tuple with three values (x-size, y-size, depth=4).

    The image files in 'fn_glob' will be sorted by name.

    Args:
          video_name (str): The name of the output video. The format is MP4.
          video_format (str): FFMPEG or MP4
          fn_glob (str): a filename glob [default='*.png']
          shape (tuple): the required shape of the images
          loop (int): number of times to loop
    """
    images = []
    for img in sorted(glob.glob(fn_glob)):
        image = imageio.imread(img)
        if not shape:
            shape = image.shape
        else:
            if not noresize:
                image = img_as_ubyte(resize(image, shape, anti_aliasing=True))
        if verbose > 1:
            console.print(f"{img}, {type(image)}, {image.shape=}")
        images.append(image)

    if verbose:
        console.print(f"Number of original images: {len(images)}")

    all_images = []
    for _ in range(loop):
        all_images.extend(images)

    if verbose:
        console.print(f"Number of concatenated images: {len(all_images)}")

    if video_format.lower() == "ffmpeg":
        kwargs = {'fps': 20, 'pixelformat': 'yuv420p'}
        imageio.mimwrite(video_name, all_images, 'FFMPEG', **kwargs)
    else:
        kwargs = {}
        imageio.mimwrite(video_name, all_images, 'MP4', **kwargs)


def parse_arguments():
    """
    Prepare the arguments that are specific for this application.
    """
    parser = argparse.ArgumentParser(
        prog="create_movie",
        description=(
            "Create an MP4 movie from the given PNG image files.\n\n"
        
            "Note that color images can be easily converted to grayscale if you set the \n"
            "last element of shape to 1."
        ),
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "--verbose", "-v",
        action="count",
        default=0,
        help=("Print verbose messages. "
              "If this option is specified multiple times, output will be more verbose.")
    )
    parser.add_argument(
        "--video-name",
        required=True,
        type=str, default="output.mp4",
        help="The name of the output video [default='output.mp4'].",
    )
    parser.add_argument(
        "--video-format",
        type=str, default="FFMPEG",
        help="The format of the output video.",
    )
    parser.add_argument(
        "--files",
        required=True,
        type=str, default="*.png",
        help="A file glob [default='*.png'].",
    )
    parser.add_argument(
        "--shape",
        type=str, default=None,
        help="The required shape to which the images will be resized, e.g. '(2186, 3496, 4)'.",
    )
    parser.add_argument(
        "--loop",
        type=int, default=1,
        help="The number of times the video has to loop over all the frames.",
    )
    parser.add_argument(
        "--noresize", "--no-resize",
        action="store_true",
        help="If all images already have the same size already.",
    )

    arguments = parser.parse_args()
    return arguments


def main():
    global verbose

    args = parse_arguments()

    verbose = args.verbose

    if args.shape:
        shape = args.shape[1:-1].split(',')
        shape = tuple(int(x) for x in shape)
        print(f"{shape=}")
    else:
        shape = None

    create_movie(args.video_name, args.video_format, args.files,
                 shape=shape, loop=args.loop, noresize=args.noresize)


console = Console()
verbose = 0

if __name__ == "__main__":
    main()
