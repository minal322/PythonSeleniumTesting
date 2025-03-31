import pytest
import time

''' Simple Fixtures
setup ---- function which is defined under fixture decorator is basically setup in avocado 
if you want some prio task to execute before some test then we can use fixtures
and 
yeild ---- Use yield in a fixture to define setup and teardown operations, 
where the code before yield is the setup and the code after yield is the teardown. 
conftest.py:like avocado here we don't have teardown function. We can use yield keyword to warp our teardown code. 
                
'''

@pytest.fixture
def simple_fixtures():
    print("Setup tasks are execute here ")
    print("Connecting to databases")
    time.sleep(2)
    print("Successfully established connection .... ")

    yield
    print("Operations completed now closing database connection")

#this test must execute setup,teardown before executing actual test
def test_exec_queries(simple_fixtures):
    print("fetch data from database")
    print("hurray done")

#using fixture from conftest
def test_conf_data():
    print("data is printed from conftest file")