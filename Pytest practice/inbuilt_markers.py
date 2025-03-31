import pytest

'''  In-buit markers
usefixtures - use fixtures on a test function or class
filterwarnings - filter certain warnings of a test function
skip - always skip a test function
skipif - skip a test function if a certain condition is met
xfail - produce an “expected failure” outcome if a certain condition is met
parametrize - perform multiple calls to the same test function.
'''
a = "hello"
b = "bye"

@pytest.mark.skip
def test_skipping():
    print("this is skipped")

@pytest.mark.skipif(a == b,reason="skipping as condition matches")
def test_skipping_with_condition():
    print("this is skipped")
    assert 1 == 1 , "Values are not equal"

def test_execute():
    print("this test is executed")

def test_exec2():
    print("this will also executed")

@pytest.mark.xfail
def test_exec_not_log():
    print("this will execute but not getl logged in reports/output")