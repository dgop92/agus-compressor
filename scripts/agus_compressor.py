import argparse

from config.logging import config_logger
from core.compress import compress_file_logging_time
from core.decompress import (
    decompress_file_in_parallel_logging_time,
    decompress_file_logging_time,
)

if __name__ == "__main__":
    config_logger()
    parser = argparse.ArgumentParser(description="A compressor decompressor utility")
    parser.add_argument("command", choices=["compress", "decompress", "verify"])
    parser.add_argument("input_file", type=str)
    parser.add_argument("output_file", type=str, nargs="?")
    parser.add_argument(
        "--n-cores",
        type=int,
        default=0,
        help="Number of cores to use. if 0, do not use multiprocessing",
    )
    args = parser.parse_args()

    if args.command == "compress":
        if args.output_file is None:
            args.output_file = "comprimido.elmejorprofesor"

        if args.n_cores == 0:
            compress_file_logging_time(args.input_file, args.output_file)
        else:
            raise NotImplementedError("Not implemented yet")
    elif args.command == "decompress":
        if args.output_file is None:
            args.output_file = "descomprimido-elmejorprofesor.txt"

        if args.n_cores == 0:
            decompress_file_logging_time(args.input_file, args.output_file)
        else:
            decompress_file_in_parallel_logging_time(
                args.input_file, args.output_file, args.n_cores
            )
