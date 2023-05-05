import logging
import pickle
import time
from multiprocessing import Pool
from typing import List

from core.dahuffman import HuffmanCodec


def decompress_file(compressed_file: str, output_file: str):
    with open(compressed_file, "rb") as file:
        logging.info(f"Reading {compressed_file}")
        compress_data = pickle.load(file)
        codec = HuffmanCodec.create_from_data(compress_data["codec_data"])

        logging.info(f"Decompressing {compressed_file} to {output_file}")
        decoded = codec.decode(compress_data["encoded"])

        with open(output_file, "w") as file:
            logging.info(f"Writing to {output_file}")
            file.write(decoded)


def decompress_content_in_parallel(
    compressed_content: List[bytes],
    codec: HuffmanCodec,
    n_cores=2,
) -> str:
    with Pool(processes=n_cores) as pool:
        results = pool.map(codec.decode, compressed_content)

    return b"".join(results)


def decompress_file_in_parallel(compressed_file: str, output_file: str, n_cores=2):
    logging.info(f"Reading {compressed_file}")
    with open(compressed_file, "rb") as f:
        compress_data = pickle.load(f)

    codec = HuffmanCodec.create_from_data(compress_data["codec_data"])

    logging.info(f"Decompressing {compressed_file} in parallel")
    decompressed_content = decompress_content_in_parallel(
        compress_data["encoded"], codec, n_cores
    )

    logging.info(f"Writing to {output_file}")
    with open(output_file, "wb") as f:
        f.write(decompressed_content)


def decompress_file_logging_time(compressed_file: str, output_file: str):
    start = time.time()
    decompress_file(compressed_file, output_file)
    end = time.time()
    logging.info(f"Decompressing {compressed_file} took {end - start} seconds")


def decompress_file_in_parallel_logging_time(
    compressed_file: str, output_file: str, n_cores=2
):
    start = time.time()
    decompress_file_in_parallel(compressed_file, output_file, n_cores)
    end = time.time()
    logging.info(f"Decompressing {compressed_file} took {end - start} seconds")
