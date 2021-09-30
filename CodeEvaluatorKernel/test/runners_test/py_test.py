import pytest
from src.config.dotenv_loader import load_dotenv_variables
from test.mock.file_mocker import generate_file
from src.runners.py_runner import run_py


def test_hello_world():
    load_dotenv_variables()

    expected = ['HELLO WORLD']

    code = '''print("HELLO WORLD");'''

    filename = generate_file(code, 'py')

    outputs = run_py(filename, None)

    assert outputs == expected
