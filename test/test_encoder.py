from pathlib import Path

from stego.decoder import Decoder
from stego.encoder import Encoder


CURRENT_DIR = Path(__file__).parent
STEGO_FILE_PATH = CURRENT_DIR / 'resources' / '~image.bmp'
IMAGE_FILE_PATH = CURRENT_DIR / 'resources' / 'image.bmp'
KEYS_FILE_PATH = CURRENT_DIR / 'resources' / 'keys.txt'


def test_encoder():

    Encoder().inject_message(
        image_file_path=str(IMAGE_FILE_PATH),
        keys_file_path=str(KEYS_FILE_PATH),
        message='Hello World!'
    )

    extracted_message = Decoder().extract_message(
        image_file_path=str(STEGO_FILE_PATH),
        keys_file_path=str(KEYS_FILE_PATH),
    )

    assert extracted_message == 'Hello World!'
