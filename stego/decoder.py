from re import findall
from typing import List, Tuple

from stego.stego_helper import (
    load_keys_file_handler,
    open_and_load_image,
    FileMode
)


class Decoder:
    """
        This class provides ability to extract message from target stego-container
        (picture) by specified key-file.
    """

    keys: List[Tuple[int, int]]
    """The list of keys to extract message from specified picture."""

    message: List[str]
    """The list of extracted symbols from stego-container (picture)."""

    def _parse_key(self, key_string: str) -> Tuple[int, int]:
        """
           This method returns parsed private key elements as tuple.

           Args:
           key_string (str): The private key string value.

           Returns:
           Tuple[int, int]: The tuple of coordinates of injected symbol.

           """

        key_digit = int(findall(r'\((\d+),', key_string)[0])
        data_digit = int(findall(r',\s(\d+)\)', key_string)[0])
        return key_digit, data_digit

    def extract_message(self, image_file_path: str, keys_file_path: str) -> str:
        """
        This method provides ability to extract message from target stego-container (picture).

        Args:
        image_file_path (str): The target stego-container image path.
        keys_file_path (str): The output file with stored private key.

        Returns:
        str: The extracted message from stego-container.

        """

        image_file = open_and_load_image(file_path=image_file_path)
        keys_file = load_keys_file_handler(file_path=keys_file_path, mode=FileMode.Read)
        keys_coordinates = [self._parse_key(key_value) for key_value in keys_file.readlines()]
        message = ''.join([
            chr(image_file.getpixel(key_value)[0])
            for key_value in keys_coordinates
        ])

        image_file.close(), keys_file.close()

        return message
