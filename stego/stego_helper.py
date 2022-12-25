from pathlib import Path
from typing import Any, IO

from PIL import Image
from enum import Enum


class FileMode(Enum):
    """There is the simplest enum forever :D. Just exploring python std!"""

    Read = 'r'
    Write = 'w+'


def open_and_load_image(file_path: str) -> Image:
    """
    Returns object contains pixels (hex-bytes) of target picture.

    Args:
    file_path (str): The target image file path.

    Returns:
    Image: The opened image object provided by PIL.

    """

    return Image.open(file_path)


def load_keys_file_handler(file_path: str, mode: FileMode) -> IO[Any]:
    """
    Returns string list with coordinates information.

    Args:
    file_path (str): The target image file path.
    mode (FileMode): The file opening mode as read/write.

    Returns:
    IO[Any]: The opened file handler.

    """

    return open(file=file_path, mode=mode.value)


def save_stego_container(image_draw, image_file: str) -> str:
    """
    This method saves stego-container image returns own file path.

    Args:
    image_draw (Image): The PIL Image object.
    image_file (str): The current image file path.

    Returns:
    str: The output file path.

    """

    current_file = Path(image_file)
    output_file = f'{current_file.parent}/~{current_file.name}'
    image_draw.save(output_file, 'BMP')
    return output_file
