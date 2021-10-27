import os


def get_tempdir() -> str:
    return os.environ['TEMP']


def get_file_separator() -> str:
    return '\\' if 'WINDOWS' in os.environ['OS'] else '/'


def get_os_name() -> str:
    return os.environ['OS']
