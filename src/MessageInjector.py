from logging import exception, info
from random import randint
from typing import IO, Any, AnyStr, List

from PIL import Image, ImageDraw


class MessageInjector(object):
    def __init__(self):
        self.keys = list()
        self.message = list()

    @staticmethod
    def _open_file(file_path: str) -> IO[Any]:
        try:
            return open(file_path, 'w+')
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

    def inject_message(self, image_path: str, keys_file_path: str, user_message: str) -> None:
        image_pixels = self._load_image_pixels(image_file_path=image_path)
        image_draw = ImageDraw.Draw(image_pixels)

        width = image_pixels.size[0]
        height = image_pixels.size[1]
        pixels = image_pixels.load()

        key_file_handler = self._load_keys_file(key_file_path=keys_file_path)

        for char in user_message:
            key = (randint(1, width - 100), randint(1, height - 100))
            green, blue = pixels[key][1:3]
            image_draw.point(key, (char, green, blue))
            key_file_handler.write(str(key) + "\n")

        image_pixels.save("140.bmp", "BMP")
        key_file_handler.close()
        print('Keys were written to the "keys.txt" file')
