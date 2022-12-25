from pathlib import Path
from typing import Any, IO

from PIL import Image
from enum import Enum


class FileMode(Enum):
    Read = 'r'
    Write = 'w+'


def open_and_load_image(file_path: str, mode: FileMode) -> Image:
    """Returns object contains pixels (hex-bytes) of target picture."""

    return Image.open(file_path)


def load_keys_file_handler(file_path: str, mode: FileMode) -> IO[Any]:
    """Returns string list with coordinates information."""

    return open(file=file_path, mode=mode.value)


def save_stego_container(image_draw, image_file: str) -> str:
    current_file = Path(image_file)
    output_file = f'{current_file.parent}/~{current_file.name}'
    image_draw.save(output_file, 'BMP')
    return output_file
