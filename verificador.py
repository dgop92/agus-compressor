import argparse

from config.logging import config_logger
from core.verify import compare_files

if __name__ == "__main__":
    config_logger()
    parser = argparse.ArgumentParser(
        description="Compare two files and return if they are the same or not"
    )
    parser.add_argument("file1", help="First file to compare")
    parser.add_argument("file2", help="Second file to compare")
    args = parser.parse_args()

    are_the_same = compare_files(args.file1, args.file2)
    if are_the_same:
        print("ok")
    else:
        print("nook")
