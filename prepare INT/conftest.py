import pytest

@pytest.fixture(scope='session',autouse=True)
def runonce():u8
    print("My fixture is callled form conftest")