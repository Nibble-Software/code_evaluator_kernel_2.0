import pytest
from pytest import fail
from src.utils.process_utils import run_process
from src.exceptions.FailedProcessError import FailedProcessError


def test_gcc():
    try:
        run_process('g++', ['-v'])
    except FailedProcessError as error:
        fail()


def test_failed_process():
    try:
        run_process('g++', ['-o'])
        fail()
    except FailedProcessError:
        pass
