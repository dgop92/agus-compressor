import argparse

from config.logging import config_logger
from core.compress import compress_file_logging_time

if __name__ == "__main__":
    config_logger()
    parser = argparse.ArgumentParser(description="A compressor utility")
    parser.add_argument("input_file", type=str)
    parser.add_argument("output_file", type=str, nargs="?")
    args = parser.parse_args()

    if args.output_file is None:
        args.output_file = "comprimido.elmejorprofesor"
    compress_file_logging_time(args.input_file, args.output_file)
