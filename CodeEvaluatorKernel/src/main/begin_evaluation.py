from src.exercise.tester import run_exercise


def begin_evaluation(language: str, solution_filepath: str, inputs: [str], outputs: [str]) -> dict:

    status, results = run_exercise(language, solution_filepath, inputs, outputs)

    overview = {
        'status': status,
        'expected': outputs,
        'got': results
    }

    return overview

