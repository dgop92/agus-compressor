import logging
import pickle
import time
from multiprocessing import Pool

from core.dahuffman import HuffmanCodec
from core.frecuencies import get_frequencies_of_text


def compress_file(text_file: str, output_file: str):
    logging.info(f"Reading {text_file}")
    with open(text_file, "r") as file:
        text = file.read()
        codec = HuffmanCodec.from_frequencies(get_frequencies_of_text(text))

        with open(output_file, "wb") as file:
            logging.info(f"Compresing {text_file} to {output_file}")
            encoded = codec.encode(text)
            logging.info(f"Writting to {output_file}")
            compress_data = {
                "codec_data": codec.get_codec_data(),
                "encoded": encoded,
            }
            pickle.dump(compress_data, file)


def compress_content_in_parallel(
    content: bytes,
    codec: HuffmanCodec,
    n_cores=2,
) -> list[bytes]:
    # Divide the content into n splits
    total_length = len(content)
    split_length = total_length // n_cores
    splits = [
        content[i : i + split_length] for i in range(0, total_length, split_length)
    ]
    if len(splits) > n_cores:
        last_split = splits.pop()
        splits[-1] += last_split

    with Pool(processes=n_cores) as pool:
        results = pool.map(codec.encode, splits)

    return results


def compress_file_in_parallel(text_file: str, output_file: str, n_cores=2):
    logging.info(f"Reading {text_file}")
    with open(text_file, "rb") as f:
        content = f.read()

    codec = HuffmanCodec.from_data(content)

    logging.info(f"Compresing {text_file} in parallel")
    compressed_content = compress_content_in_parallel(content, codec, n_cores)

    logging.info(f"Writting to {output_file}")
    with open(output_file, "wb") as f:
        compress_data = {
            "codec_data": codec.get_codec_data(),
            "encoded": compressed_content,
        }
        pickle.dump(compress_data, f)


def compress_file_logging_time(text_file: str, output_file: str):
    start = time.time()
    compress_file(text_file, output_file)
    end = time.time()
    logging.info(f"Compressing {text_file} took {end - start} seconds")


def compress_file_in_parallel_logging_time(text_file: str, output_file: str, n_cores=2):
    start = time.time()
    compress_file_in_parallel(text_file, output_file, n_cores)
    end = time.time()
    logging.info(f"Compressing {text_file} took {end - start} seconds")
