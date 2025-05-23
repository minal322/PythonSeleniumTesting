import pytest
class TestScope:
    @pytest.fixture(scope='class',autouse=True)
    def myfixture(self):
        print("Running only once")

    def test_method3(self):
        print("Hello method 3 ")

    def test_method4(self):
        print("Hello method 4")