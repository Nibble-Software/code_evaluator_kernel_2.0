from src.exercise.tester import run_exercise
from src.config.dotenv_loader import load_dotenv_variables


def begin_evaluation(language: str, solution_filepath: str, inputs: [str], outputs: [str]) -> dict:
    load_dotenv_variables()

    status, results = run_exercise(language, solution_filepath, inputs, outputs)

    overview = {
        'status': status,
        'expected': outputs,
        'got': results
    }

    print(overview)

    return overview
