from src.utils.os_utils import get_tempdir,get_file_separator


def generate_file(code: str,extension: str) -> str:
    tempdir = get_tempdir()

    separator = get_file_separator()

    filename = f'{tempdir}{separator}file.{extension}'

    file = open(filename, 'w')

    file.write(code)

    file.close()

    return filename
