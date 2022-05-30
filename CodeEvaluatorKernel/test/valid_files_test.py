from src.utils.language_utils import is_supported_language


def test_valid_cpp_language():
    assert is_supported_language('c++') is True


def test_valid_python_language():
    assert is_supported_language('python') is True


def test_invalid_javascript_language():
    assert is_supported_language('javascript') is False
