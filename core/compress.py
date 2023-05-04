import logging
import pickle
import time

from core.dahuffman import HuffmanCodec


def compress_file(text_file: str, output_file: str):
    logging.info(f"Reading {text_file}")
    with open(text_file, "rb") as file:
        content = file.read()
        codec = HuffmanCodec.from_data(content)

        with open(output_file, "wb") as file:
            logging.info(f"Compresing {text_file} to {output_file}")
            encoded = codec.encode(content)
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
