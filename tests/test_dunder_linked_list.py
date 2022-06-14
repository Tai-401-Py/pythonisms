import pytest
from pythonisms.dunder_linked_list import LinkedList, TargetError


def test_init():
    data = ['apple','banana', 'cucumber']
    linked_list = LinkedList(data)

    assert str(linked_list) == "{ apple } -> { banana } -> { cucumber } -> NULL"


def test_iter():

    data = ['apple','banana', 'cucumber']
    linked_list = LinkedList(data)

    assert list(linked_list) == data

def test_len():

    data = ['apple','banana', 'cucumber']
    linked_list = LinkedList(data)

    assert len(linked_list) == 3

def test_print():

    data = ['apple','banana', 'cucumber']
    linked_list = LinkedList(data)

    assert print(linked_list) == print("{ apple } -> { banana } -> { cucumber } -> NULL")

def test_get():
    
    data = ['apple','banana', 'cucumber']
    linked_list = LinkedList(data)

    assert linked_list[0] == 'apple'

def test_bad_get():

    data = ['apple','banana', 'cucumber']
    linked_list = LinkedList(data)

    with pytest.raises(TargetError):
        return linked_list[5]
    
def test_get_neg():
    data = ['apple','banana', 'cucumber']
    linked_list = LinkedList(data)
    assert linked_list[-1] == 'cucumber'

