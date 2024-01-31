"""Applying multiple decorators to a single function

Note: When stacking decorators, it's a common practice to use functools.wraps
to ensure that the metadata of the original function is preserved throughout 
the stacking process. This helps maintain clarity and consistency in debugging 
and understanding the properties of the decorated function.
"""

import functools

def split_string(function):
    @functools.wraps(function)
    def wrapper():
        func: str = function()
        splitted_string = func.split()
        return splitted_string
    
    return wrapper

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    
    return wrapper

@split_string
@uppercase_decorator
def say_hi():
    return 'hello there'

print(say_hi())
