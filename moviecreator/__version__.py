"""
The one and only place for the version number.

This file is used by
"""
VERSION = (0, 1, 10)

__version__ = '.'.join(map(str, VERSION))

if __name__ == "__main__":
    print(f"v{__version__}")
