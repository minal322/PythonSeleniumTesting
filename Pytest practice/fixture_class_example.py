import pytest

#insted of adding fixture for each method in class , we can keep scope of fixture to class
#using fixtures for class
'''
Use fixture for class scope
@pytest.mark.usefixtures("setup")
class TestDemoFixtures:

    def test_exec_queries(self):
        print("fetch data from database")
        print("hurray done")

    def test_method1(self):
        print("method 1")

    def test_method2(self):
        print("method 3")

'''
#without class scope
@pytest.mark.usefixtures("setup")
class TestDemoFixtures:

    def test_exec_queries(self):
        print("fetch data from database")
        print("hurray done")

    def test_method1(self):
        print("method 1")

    def test_method2(self):
        print("method 3")

# def test_exec_queries(setup):
#     print("fetch data from database")
#     print("hurray done")
#
# def test_method1(setup):
#     print("method 1")
#
# def test_method2(setup):
#     print("method 3")