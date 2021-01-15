"""Setup script for tcs-stamp-converter"""
import os
import pathlib

from setuptools import setup

# Package meta-data.

NAME = "movie_creator"
PACKAGE_NAME = "moviecreator"
DESCRIPTION = "Creates a movie from a list of image files."
URL = "https://github.com/rhuygen/movie_creator"
EMAIL = "rik.huygen@kuleuven.be"
AUTHOR = "Rik Huygen"
REQUIRES_PYTHON = '>=3.8.0'
VERSION = None

# The directory containing this file

HERE = pathlib.Path(__file__).parent

# The text of the README file

README = (HERE / "README.md").read_text()

# Load the requirements

REQUIREMENTS = (HERE / "requirements.txt").read_text().split()

# Load the package's __version__.py module as a dictionary.

about = {}
if VERSION is None:
    with open(os.path.join(HERE, PACKAGE_NAME, '__version__.py')) as f:
        exec(f.read(), about)
        VERSION = about['__version__']


# This call to setup() does all the work

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    url=URL,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["moviecreator"],
    install_requires=REQUIREMENTS,
    entry_points={
        "console_scripts": [
            "create_movie=moviecreator.create_movie:main",
        ]
    },
)
