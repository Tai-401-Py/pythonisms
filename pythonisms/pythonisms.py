import re
import string
import time
from functools import wraps

# Start Wraps
def timed_method(func):
    '''
    Wrapper times the amount of time it takes to complete a method
    '''
    def wrapper(*args, **kwargs):
        ts = time.time()
        result = func(*args,**kwargs)
        te = time.time()
        print(f'{func.__name__} took {te-ts} seconds to complete')
        return result
    return wrapper


class Pythonisms:
    '''
    Pythonisms practicing the dunder methods
    '''
    def __init__(self, collection):
        self.collection = collection

    def __str__(self):
        string ="The current items in the collection are as follows:"
        for item in self.collection:
            string += f" {item}"
        return string

    @timed_method       
    def sum_collection(self):
        if not self.collection:
            return 'There is no collection to add!'
        for item in self.collection:
            response = None
            try:
                if item.type() == string:
                    response += f'{item} '
                if item.type()== int or float:
                    response += item
                if item.type() == bool:
                    return('Can not sum a boolean value')
            except:
                return('Unable to comply with your request, you may be mixing object types in collection')
                


