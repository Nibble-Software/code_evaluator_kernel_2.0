from src.runners.cpp_runner import run_cpp

supported_languages = {
    'c++': {
        'extension': 'cpp',
        'run': run_cpp
    },
    'python': {
        'extension': 'py'
    }

}
