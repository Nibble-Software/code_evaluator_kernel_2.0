from src.utils.process_utils import run_code


def run_py(filepath: str, inputs: list[str]) -> [str]:
    return run_code('python', [filepath], inputs)
