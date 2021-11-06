from re import findall
from logging import exception
from typing import (
    IO,
    Any,
    AnyStr,
    List,
    Tuple
)

from PIL import Image


class MessageExtractor(object):
    """
        This class provides ability to extract message from target stego-container
        (picture) by specified key-file.

        Attributes
        ----------
        keys : List[AnyStr]
            The list of keys to extract message from specified picture.
        message : List[AnyStr]
            The list of extracted symbols from stego-container (picture).

        Methods
        -------
        _open_file(file_path: str) -> IO[Any]
            Returns OI[Any] (file handler) by specified file path.
        _load_image_pixels(self, image_file_path: str)
            Returns object contains pixels (hex-bytes) of target picture.
        _load_keys_file(self, key_file_path: str) -> List[AnyStr]
            Returns List[AnyStr] of specified file which contains key.
        _key_transform(key_string: str, index: int) -> Tuple[int, int]
            Returns Tuple[int, int] of key coordinates to get stored symbol.
        extract_message(self, image_path: str, keys_file_path: str) -> AnyStr
            This method provides ability to get stored message from specified
            picture by key-file.
    """

    def __init__(self):
        self.keys = list()
        self.message = list()

    @staticmethod
    def _open_file(file_path: str) -> IO[Any]:
        try:
            return open(file_path, 'r')
        except FileExistsError or FileNotFoundError as e:
            exception(f"Error while opening/reading specified file: {file_path}")
            raise e

    def _load_image_pixels(self, image_file_path: str):
        image_handler = self._open_file(file_path=image_file_path)
        image = Image.open(image_handler)
        return image.load()

    def _load_keys_file(self, key_file_path: str) -> List[AnyStr]:
        keys_file_handler = self._open_file(file_path=key_file_path)
        return [line.strip() for line in keys_file_handler]

    @staticmethod
    def _key_transform(key_string: str, index: int) -> Tuple[int, int]:
        key_digit = int(findall(r'\((\d+),', key_string)[index])
        data_digit = int(findall(r',\s(\d+)\)', key_string)[index])
        return tuple(key_digit, data_digit)

    def extract_message(self, image_path: str, keys_file_path: str) -> AnyStr:
        image_pixels = self._load_image_pixels(image_file_path=image_path)

        user_key = self._load_keys_file(key_file_path=keys_file_path)
        key_string = str(user_key)

        key_num_length = len(findall(r'\((\d+),', key_string))

        self.keys = [self._key_transform(key_string, i) for i in range(key_num_length)]
        self.message = [image_pixels[tuple(key)[0]] for key in self.keys]

        return ''.join([chr(elem) for elem in self.message])
