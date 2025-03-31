import pytest

'''
Custom marker - which is user defined marker.
Here create two custom markers smoke,smoke2
to run specific test using markers then syntax is 
pytest filename.py -m smoke -v -s
OR
pytest filename.py -m smoke2 -v -s 
'''

@pytest.mark.smoke
def test_one():
    print("First test")

@pytest.mark.smoke2
def test_two():
    print("second test")

@pytest.mark.smoke
def test_three():
    print("third test")