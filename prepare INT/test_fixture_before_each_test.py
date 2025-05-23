# How to run a specific method before each test method in a class using fixture
import pytest

class TestFixture:

    @pytest.fixture(scope='function', autouse=True)
    def calling(self):
        print("Helo from fixture")

    def test_method1(self):
        print("Hello method 1 ")

    def test_method2(self):
        print("Hello method 2")