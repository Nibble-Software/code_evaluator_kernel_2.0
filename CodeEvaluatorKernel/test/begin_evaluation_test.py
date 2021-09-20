import pytest
from src.main.begin_evaluation import begin_evaluation
from test.mock.file_mocker import generate_file
from src.config.dotenv_loader import load_dotenv_variables


def test_success_on_hello_world_cpp():

    load_dotenv_variables()

    outputs = ['HELLO WORLD']

    expected = {
        'status': 'PASSED',
        'expected': outputs,
        'got': outputs
    }

    code = '''
    #include <stdio.h>
    int main(){
        printf("HELLO WORLD");
        return 0;
    }'''

    filename = generate_file(code, 'cpp')

    overview = begin_evaluation('c++', filename, None, outputs)

    assert expected == overview


def test_failed_on_hello_world_cpp():

    load_dotenv_variables()

    outputs = ['BYE WORLD']

    expected = {
        'status': 'FAILED',
        'expected': outputs,
        'got': ['HELLO WORLD']
    }

    code = '''
    #include <stdio.h>
    int main(){
        printf("HELLO WORLD");
        return 0;
    }'''

    filename = generate_file(code, 'cpp')

    overview = begin_evaluation('c++', filename, None, outputs)

    assert expected == overview


def test_compilation_error_on_hello_world_cpp():

    load_dotenv_variables()

    outputs = ['HELLO WORLD']

    expected = {
        'status': 'COMPILATION_ERROR',
        'expected': outputs,
        'got': []
    }

    code = '''
    #include <stdio.h>
    int main(){
        printf("HELLO WORLD")
        return 0;
    }'''

    filename = generate_file(code, 'cpp')

    overview = begin_evaluation('c++', filename, None, outputs)

    assert expected == overview


def test_correct_sum_in_cpp():

    load_dotenv_variables()

    outputs = ['5', '7', '0']

    inputs = ['3', '2 3', '6 1', '1 -1']

    expected = {
        'status': 'PASSED',
        'expected': outputs,
        'got': outputs
    }

    code = '''
    #include <stdio.h>
    int main(){
        int a,b,num;
        
        scanf("%d",&num);
        
        for(int i = 0; i < num ; i++){
            scanf("%d",&a);
            scanf("%d",&b);
            
            printf("%d\\n",a+b);
            
        
        }
    
    }
    '''

    filename = generate_file(code, 'cpp')

    overview = begin_evaluation('c++', filename, inputs, outputs)

    assert overview == expected


def test_incorrect_sum_in_cpp():
    load_dotenv_variables()

    outputs = ['5', '7', '0']

    inputs = ['3', '2 3', '6 1', '1 -1']

    expected = {
        'status': 'FAILED',
        'expected': outputs,
        'got': ['-1', '5', '2']
    }

    code = '''
    #include <stdio.h>
    int main(){
        int a,b,num;

        scanf("%d",&num);

        for(int i = 0; i < num ; i++){
            scanf("%d",&a);
            scanf("%d",&b);

            printf("%d\\n",a-b);


        }

    }
    '''

    filename = generate_file(code, 'cpp')

    overview = begin_evaluation('c++', filename, inputs, outputs)

    assert overview == expected


def test_compilation_error_sum_in_cpp():
    load_dotenv_variables()

    outputs = ['5', '7', '0']

    inputs = ['3', '2 3', '6 1', '1 -1']

    expected = {
        'status': 'COMPILATION_ERROR',
        'expected': outputs,
        'got': []
    }

    code = '''
    #include <stdio.h>
    int main(){
        int a,b,num;

        scanf("%d",&num)

        for(int i = 0; i < num ; i++){
            scanf("%d",&a);
            scanf("%d",&b);

            printf("%d\\n",a-b);


        }

    }
    '''

    filename = generate_file(code, 'cpp')

    overview = begin_evaluation('c++', filename, inputs, outputs)

    assert overview == expected


def test_timeout_error_sum_in_cpp():
    load_dotenv_variables()

    outputs = ['5', '7', '0']

    inputs = ['3', '2 3', '6 1', '1 -1']

    expected = {
        'status': 'TIMEOUT_ERROR',
        'expected': outputs,
        'got': []
    }

    code = '''
    #include <stdio.h>
    int main(){
        int a,b,num;

        scanf("%d",&num);

        for(int i = 0; i < num ; i++){
            scanf("%d",&a);
            scanf("%d",&b);

            printf("%d\\n",a-b);


        }
        while(1);
        
        return 0;

    }
    '''

    filename = generate_file(code, 'cpp')

    overview = begin_evaluation('c++', filename, inputs, outputs)

    assert overview == expected
