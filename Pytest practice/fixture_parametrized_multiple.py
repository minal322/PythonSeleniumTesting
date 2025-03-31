import pytest


def test_demo1(param_demo1):
    print("Data fetched from params")
    print(param_demo1)

def test_Browser_data(cross_browser):
    print("Cross Browser example")
    print(cross_browser)
    print("1st parameter "+ cross_browser[0])
    print("2nd parameter "+ cross_browser[1])