import pytest
from pytest import fail
from src.config.dotenv_loader import load_dotenv_variables
from src.exceptions.CompilationError import CompilationError
from src.runners.cpp_runner import compile_cpp, run_cpp
from test.mock.file_mocker import generate_file
from src.exceptions.CodeTimeoutError import CodeTimeoutError


def test_compile_cpp():
    load_dotenv_variables()

    hello_world: str = '''
    #include <stdio.h>
    int main(){
        printf("HELLO WORLD");
        return 0;
    }
    '''

    filename = generate_file(hello_world, 'cpp')

    compile_cpp(filename)


def test_hello_world():
    load_dotenv_variables()

    expected: str = 'HELLO WORLD'

    hello_world: str = '''
    #include <stdio.h>
    int main(){
        printf("HELLO WORLD");
        return 0;
    }
    '''

    filename = generate_file(hello_world, 'cpp')

    results: [str] = run_cpp(filename, None)

    assert results[0] == expected


def test_infinite_loop():
    load_dotenv_variables()

    expected: str = 'HELLO WORLD'

    hello_world: str = '''
        #include <stdio.h>
        int main(){
            while(1);
        }
        '''

    filename: str = generate_file(hello_world,'cpp')

    try:
        results: [str] = run_cpp(filename, None)

        fail()

    except CodeTimeoutError:
        pass


def     test_addition():
    load_dotenv_variables()

    expected: str = '5'

    inputs: [str] = ['2', '3']

    code = '''
    #include <stdio.h>
    int main(){
        int a,b;
        scanf("%d",&a);
        scanf("%d",&b);
        printf("%d",a+b);
        return 0;
    }
    '''

    filename = generate_file(code, 'cpp')

    results: [str] = run_cpp(filename, inputs)

    print(results)

    assert results[0] == expected


def test_addition_infinite_loop():
    load_dotenv_variables()

    try:
        expected: str = '5'

        inputs: [str] = ['2,', '3']

        code = '''
            #include <stdio.h>
            int main(){
                int a,b;
                scanf("%d",&a);
                scanf("%d",&b);
                printf("%d",a+b);
                while(1);
                return 0;
            }
            '''

        filename = generate_file(code, 'cpp')

        results: [str] = run_cpp(filename, inputs)

        fail()

    except CodeTimeoutError as error:
        pass

    except Exception as error2:
        fail('It should raise a timeout')


def test_failed_compilation():
    try:
        load_dotenv_variables()

        code = '''
    #include <stdio.h>
    int main(){
        printf("HELLO WORLD")
        return 0;
    }
    '''

        filename = generate_file(code, 'cpp')

        results = run_cpp(filename, None)

        fail('It should raise a compilation exception')

    except CompilationError as compilation_error:
        pass