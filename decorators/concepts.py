"""The following concepts form the basis of decorators
"""
# assigning functions to variables

def plus_one(number: int) -> int:
    return number + 1;

add_one: int = plus_one
print(add_one(233)) # output should be 234


# functions inside other functions

def plus_one(number: int) -> int:
    def add_one(number: int) -> int:
        return number + 1
    result: int = add_one(number)
    return result

print(plus_one(4)) # output should be 5

# Passing Functions as Arguments to other Functions

def plus_one(number: int) -> int:
    return number + 1;

def function_call(func) -> int:
    number_to_add = 5
    return func(number_to_add)

print(function_call(plus_one)) # output should be 6


# Functions Returning other Functions

def hello_function():
    def say_hi():
        return 'Hi'
    return say_hi

hello = hello_function()
print(hello())


# Nested Functions have access to the enclosing Function's Variable Scope

def print_message(message):
    # enclosing function
    def message_sender():
        # nested function
        print(message)
    return message_sender()

print_message("Goodmorning Mr. West!")
