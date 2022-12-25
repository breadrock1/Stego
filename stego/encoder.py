from random import randint
from typing import List

from PIL import ImageDraw

from stego.stego_helper import (
    open_and_load_image,
    load_keys_file_handler,
    save_stego_container,
    FileMode
)


class Encoder:
    """
        This class provides ability to inject specified message to target stego-container
        (picture). When procedure finish successful then created key-file which contains
        coordinates data with stored message symbols.
    """

    keys: List[str]
    """The list of keys to extract message from specified picture."""

    message: List[str]
    """The list of extracted symbols from stego-container (picture)."""

    def inject_message(self, image_file_path: str, keys_file_path: str, message: str) -> str:
        """
        This method provides ability to inject specified message to target stego-container (picture).

        Args:
        image_file_path (str): The target stego-container image path.
        keys_file_path (str): The output file to store private key.
        message (str): The target message to inject to stego-container.

        Returns:
        str: The output file path with private key.

        """

        keys_file = load_keys_file_handler(file_path=keys_file_path, mode=FileMode.Write)
        image_file = open_and_load_image(file_path=image_file_path, mode=FileMode.Write)
        image_draw = ImageDraw.Draw(image_file)

        width, height = image_file.size
        pixels = image_file.load()

        for symbol in message:
            key_coordinate = (randint(1, width - 100), randint(1, height - 100))
            green, blue = pixels[key_coordinate][1:3]
            image_draw.point(key_coordinate, (ord(symbol), green, blue))
            keys_file.write(f'{key_coordinate}\n')

        output_file = save_stego_container(image_draw=image_file, image_file=image_file_path)
        image_file.close(), keys_file.close()

        return output_file
