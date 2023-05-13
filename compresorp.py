import argparse
import logging
import pickle
import time

from mpi4py import MPI

from config.logging import config_logger
from core.dahuffman import HuffmanCodec

if __name__ == "__main__":
    config_logger()
    parser = argparse.ArgumentParser(description="A compressor utility")
    parser.add_argument("input_file", type=str)
    parser.add_argument("output_file", type=str, nargs="?")
    args = parser.parse_args()

    start = 0
    end = 0

    if args.output_file is None:
        args.output_file = "comprimido.elmejorprofesor"

    text_file = args.input_file
    output_file = args.output_file

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if rank == 0:
        start = time.time()
        logging.info(f"Reading {text_file}")
        with open(text_file, "rb") as f:
            content = f.read()

        # split content
        total_length = len(content)
        split_length = total_length // size
        splits = [
            content[i : i + split_length] for i in range(0, total_length, split_length)
        ]
        if len(splits) > size:
            last_split = splits.pop()
            splits[-1] += last_split

        codec = HuffmanCodec.from_data(content)
        content_with_codec = [(codec, split) for split in splits]
    else:
        content_with_codec = None

    content_with_codec = comm.scatter(content_with_codec, root=0)

    logging.info(f"Compressing {rank}")
    codec, content = content_with_codec
    compressed = codec.encode(content)

    compressed_content = comm.gather(compressed, root=0)

    if rank == 0:
        logging.info(f"Writing {output_file}")
        with open(output_file, "wb") as f:
            compress_data = {
                "codec_data": codec.get_codec_data(),
                "encoded": compressed_content,
            }
            pickle.dump(compress_data, f)

        end = time.time()
        print(end - start)
