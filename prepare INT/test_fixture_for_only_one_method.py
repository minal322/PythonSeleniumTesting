
import pytest

class TestFixture:

    @pytest.fixture(scope='function')
    def calling(self):
        print("Helo from fixture")
    def test_method1(self,calling):
        print("Hello method 1 ")

    @pytest.mark.parametrize("names",("minu",'sham','krishna','shiv'))
    def test_names(self,names):
        print(names)

    @pytest.mark.parametrize("username, password",[("minu","@123"),("abc","@456"),("khg","@8965")])
    def test_method2(self,username,password):
        print(username)
        print(password)
        print("Hello method 2")