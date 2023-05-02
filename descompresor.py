import argparse

from config.logging import config_logger
from core.decompress import decompress_file_logging_time

if __name__ == "__main__":
    config_logger()
    parser = argparse.ArgumentParser(description="A compressor decompressor utility")
    parser.add_argument("input_file", type=str, nargs="?")
    parser.add_argument("output_file", type=str, nargs="?")
    args = parser.parse_args()

    if args.input_file is None:
        args.input_file = "comprimido.elmejorprofesor"

    if args.output_file is None:
        args.output_file = "descomprimido-elmejorprofesor.txt"

    decompress_file_logging_time(args.input_file, args.output_file)
