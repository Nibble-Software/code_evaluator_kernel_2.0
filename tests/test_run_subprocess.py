import pytest
from pytest import fail
from code_kernel_utils.process_utils import run_process
from code_kernel_exceptions.FailedProcessError import FailedProcessError


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
