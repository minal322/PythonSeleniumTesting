import pytest
@pytest.mark.usefixtures("data")

class  TestExample2:
    #fixture that returns data
    def test_editProfiles(self,data):
        print("data from fixture is")
        print(data[0])
        print(data[2])
