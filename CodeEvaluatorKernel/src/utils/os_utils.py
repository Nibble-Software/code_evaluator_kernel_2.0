import os


def get_tempdir() -> str:
    return os.environ['TEMP_LOCATION']


def get_file_separator() -> str:
    return '\\' if os.environ['OS_NAME'] == 'WINDOWS' else '/'


def get_os_name() -> str:
    return os.environ['OS_NAME']
