import pytest
from pytest import fail
from src.utils.language_utils import get_file_extension
from src.exceptions.UnsupportedLanguageError import UnsupportedLanguageError


def test_get_cpp_extension():
    assert get_file_extension('c++') == 'cpp'


def test_get_py_extension():
    assert get_file_extension('python') == 'py'


def test_get_unsupported_language_extension():
    try:
        get_file_extension('javascript')
        fail()
    except UnsupportedLanguageError as error:
        pass
