import argparse
import logging
import pickle
import time

from mpi4py import MPI

from config.logging import config_logger
from core.balancer import distribute_compressed_parts
from core.dahuffman import HuffmanCodec

if __name__ == "__main__":
    config_logger()
    parser = argparse.ArgumentParser(description="A decompressor utility")
    parser.add_argument("input_file", type=str, nargs="?")
    parser.add_argument("output_file", type=str, nargs="?")
    args = parser.parse_args()

    if args.input_file is None:
        args.input_file = "comprimido.elmejorprofesor"

    if args.output_file is None:
        args.output_file = "descomprimido-elmejorprofesor.txt"

    start = 0
    end = 0

    if args.output_file is None:
        args.output_file = "comprimido.elmejorprofesor"

    compressed_file = args.input_file
    output_file = args.output_file

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if rank == 0:
        start = time.time()
        logging.info(f"Reading {compressed_file}")
        with open(compressed_file, "rb") as f:
            compress_data = pickle.load(f)

        codec = HuffmanCodec.create_from_data(compress_data["codec_data"])
        compressed_parts = compress_data["encoded"]
        balanced_compressed_parts = distribute_compressed_parts(compressed_parts, size)
        content_with_codec = [(codec, part) for part in balanced_compressed_parts]
    else:
        content_with_codec = None

    content_with_codec = comm.scatter(content_with_codec, root=0)

    logging.info(f"Decompressing {rank}")
    codec, rank_compressed_parts = content_with_codec

    if len(rank_compressed_parts) == 0:
        rank_decompressed = None
    else:
        rank_decompressed = b"".join(
            codec.decode(part) for part in rank_compressed_parts
        )

    decompressed_content_parts = comm.gather(rank_decompressed, root=0)

    if rank == 0:
        decompressed_content = b"".join(
            filter(lambda x: x is not None, decompressed_content_parts)
        )
        logging.info(f"Writing to {output_file}")
        with open(output_file, "wb") as f:
            f.write(decompressed_content)

        end = time.time()
        print(end - start)
