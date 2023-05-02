import logging
import pickle
import time

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


def compress_file_logging_time(text_file: str, output_file: str):
    start = time.time()
    compress_file(text_file, output_file)
    end = time.time()
    print(f"Compressing {text_file} took {end - start} seconds")
