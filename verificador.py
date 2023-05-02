import argparse

from config.logging import config_logger
from core.verify import compare_files

if __name__ == "__main__":
    config_logger()
    parser = argparse.ArgumentParser(
        description="Compare file to descomprimido-elmejorprofesor.txt"
    )
    parser.add_argument("file", type=str)
    args = parser.parse_args()

    are_the_same = compare_files("descomprimido-elmejorprofesor.txt", args.file)
    if are_the_same:
        print("ok")
    else:
        print("nook")
