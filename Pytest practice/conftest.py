import pytest

#A special file where you can store fixtures that are shared across multiple test files.
##@pytest.fixture(scope="class")
@pytest.fixture
def setup():
    print("Setup tasks ")
    print("Connecting to databases")
    print("Successfully established connection .... ")

    yield
    print("teardown tasks")
    print("Operations completed now closing database connection")

#fixture that return data
@pytest.fixture()
def data():
    print("user profile data is being crerated")
    return ["Minal", "patil", "female"]

#parametrized fixture (params)
#request is only used whem params(parameterized ) fixtures are used
@pytest.fixture(params=["Minallll","Rajendra","Patil"])
def param_demo1(request):
    print("Parametrized fixture")
    return request.param

#parametrized fixture (params) --- with multiple values for one iteration
#request is only used whem params(parameterized ) fixtures are used
# here we can send more than one value as a input in the form of TUPLE
@pytest.fixture(params=[("chrome","Minal","female"),("edge","Rajendra"),("firefox", "Rajesh","male")])
def cross_browser(request):
    print("Parametrized fixture")
    return request.param