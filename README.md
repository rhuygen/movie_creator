# A movie Creator

This package provides a script to create a movie from a list of files. The idea to create this package came from the need in our group to glue together figures to form a movie that can be shown in a PowerPoint presentation. It's was too difficult to search and install new versions of `ffmpeg` and make sure to remember all the right commandline options.

## Install

    pip install movie-creator

## Usage

    $ create_movie -h
    usage: create_movie [-h] [--verbose] --video-name VIDEO_NAME [--video-format VIDEO_FORMAT] --files FILES [--shape SHAPE]
                        [--fps FPS] [--loop LOOP] [--noresize]
    
    Create an MP4 movie from the given PNG image files.
    
    Note that color images can be easily converted to grayscale if you set the 
    last element of shape to 1.
    
    optional arguments:
      -h, --help            show this help message and exit
      --verbose, -v         Print verbose messages. If this option is specified multiple times, output will be more verbose.
      --video-name VIDEO_NAME
                            The name of the output video [default='output.mp4'].
      --video-format VIDEO_FORMAT
                            The format of the output video.
      --files FILES         A file glob [default='*.png']. Should be put in single quotes.
      --shape SHAPE         The required shape to which the images will be resized, e.g. '(2186, 3496, 4)'.
      --fps FPS             The number of frames per second [default=20].
      --loop LOOP           The number of times the video has to loop over all the frames [default=1].
      --noresize, --no-resize
                            Don't resize if all images already have the same size.
    
## Description

All images need to be of the same size to produce a nice movie. Therefore, they will be resized unless you specify otherwise. If the shape argument is not given, all images will be resized to the shape of the first image.

Please note the image shape is a tuple with three values (x-size, y-size, depth=4).

The image files that are generated from the glob `'--files'` will be sorted by name.

## Examples

The following command will concatenate all the screenshots of today (2021-01-15) into a movie with just one frame per second.

    create_movie --video-name output.mp4 --files 'Screenshot 2021-01-15*.png' --noresize --fps=1
