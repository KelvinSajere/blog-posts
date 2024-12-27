import time
from pytest import fixture


@fixture
def setup():
    time.sleep(30)


import pytest


# pytest src/python/tests/calculator_lib --durations=0

# pants test src/python/tests/calculator_lib:tests
