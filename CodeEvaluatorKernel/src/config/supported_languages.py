from src.runners.cpp_runner import run_cpp
from src.runners.py_runner import run_py

supported_languages = {
    'c++': {
        'extension': 'cpp',
        'run': run_cpp
    },
    'python': {
        'extension': 'py',
        'run': run_py
    }

}
