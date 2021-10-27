from src.exceptions.MissingOutputsError import MissingOutputsError
from src.utils.process_utils import run_process, run_code
from src.utils.os_utils import get_tempdir, get_file_separator, get_os_name
from src.exceptions.FailedProcessError import FailedProcessError
from src.exceptions.CompilationError import CompilationError


def run_cpp(filepath: str, inputs: [str]) -> [str]:

    executable_path = compile_cpp(filepath)

    outputs = run_code(executable_path, None, inputs)

    return outputs


def compile_cpp(filepath: str):
    try:
        tempdir = get_tempdir()

        separator = get_file_separator()

        extension = 'exe' if get_os_name() == 'WINDOWS' else 'out'

        executable_path = f'{tempdir}{separator}a.{extension}'

        run_process('g++', [filepath, '-o', executable_path])

        return executable_path

    except FailedProcessError as error:

        raise CompilationError()
