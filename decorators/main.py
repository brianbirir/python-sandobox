"""Actual decorator implementation"""

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    
    return wrapper

# applying decorator as function assigned to a variable

def say_hi():
    return 'hello there'

decorate = uppercase_decorator(say_hi)
print(decorate())

# using @ symbol to apply the decorator

@uppercase_decorator
def say_hi():
    return 'Whozzap!'

print(say_hi())