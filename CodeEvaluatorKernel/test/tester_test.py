import pytest
from src.config.dotenv_loader import load_dotenv_variables
from src.exercise.tester import run_exercise
from test.mock.file_mocker import generate_file


def test_success_on_hello_world():
    msg_expected = 'PASSED'
    results_expected = ['HELLO WORLD']

    load_dotenv_variables()

    code = '''
    #include <stdio.h>
    int main(){
        printf("HELLO WORLD");
        return 0;
    }'''

    filename = generate_file(code, 'cpp')

    msg, results = run_exercise('c++', filename, None, ['HELLO WORLD'])

    assert msg == msg_expected

    assert results_expected == results


def test_fail_on_hello_world():
    msg_expected = 'FAILED'

    results_expected = ['BYE WORLD']

    load_dotenv_variables()

    code = '''
    #include <stdio.h>
    int main(){
        printf("HELLO WORLD");
        return 0;
    }'''

    filename = generate_file(code, 'cpp')

    msg, results = run_exercise('c++', filename, None, ['BYE WORLD'])

    assert msg == msg_expected

    assert results_expected != results


def test_compilation_error_on_hello_world():
    msg_expected = 'COMPILATION_ERROR'

    results_expected = []

    load_dotenv_variables()

    code = '''
    #include <stdio.h>
    int main(){
        printf("HELLO WORLD")
        return 0;
    }'''

    filename = generate_file(code, 'cpp')

    msg, results = run_exercise('c++', filename, None, ['HELLO WORLD'])

    assert msg == msg_expected

    assert results_expected == results
