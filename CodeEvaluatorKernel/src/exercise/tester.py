from src.utils.language_utils import get_runner
from src.exceptions.CompilationError import CompilationError
from src.exceptions.ExecutionError import ExecutionError
from src.exceptions.CodeTimeoutError import CodeTimeoutError

status: [str] = ['PASSED', 'FAILED', 'COMPILATION_ERROR', 'EXECUTION_ERROR', 'TIMEOUT_ERROR']


def run_exercise(language: str, solution_filepath: str, inputs: [str], outputs: [str]) -> (str, [str]):
    try:
        results = get_runner(language)(solution_filepath,inputs)
        if outputs == results:
            return status[0], results
        else:
            return status[1], results

    except CompilationError as compilation_error:
        return status[2], []

    except ExecutionError as execution_error:
        return status[3], []

    except CodeTimeoutError as error:
        return status[4],[]

    except Exception as exeption:
        raise exeption

