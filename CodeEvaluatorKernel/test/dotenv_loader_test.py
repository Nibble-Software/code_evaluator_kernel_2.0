from src.config.dotenv_loader import load_dotenv_variables
import os


def test_load_dotenv():
    try:
        load_dotenv_variables()
    except Exception as error:
        print(error)
        raise Exception


def test_dotenv_variable():
    load_dotenv_variables()

    temp_location = os.environ['TEMP_LOCATION']

    print(f'\nTEMP_LOCATION={temp_location}')

    assert temp_location is not None
