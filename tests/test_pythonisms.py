import pytest as pytest
from pythonisms.pythonisms import Pythonisms

def test_exists():
    assert Pythonisms

def test_str():

    collection = Pythonisms(['arugula', 'beans', 'carrot'])

    assert str(collection) == "The current items in the collection are as follows: arugula beans carrot"

def test_integer_collection():
    collection = Pythonisms((1,2,3))
    assert str(collection) == "The current items in the collection are as follows: 1 2 3"

def test_no_collection_sum():
    collection = Pythonisms([])
    response = collection.sum_collection()
    expected = 'There is no collection to add!'
    assert response == expected