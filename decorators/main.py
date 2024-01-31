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


# Accepting Arguments in Decorator Functions

def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print(f'My arguments are: {arg1}, {arg2}')
        function(arg1, arg2)

    return wrapper_accepting_arguments


@decorator_with_arguments
def cities(city_one, city_two):
    print(f'Cities I love are {city_one} and {city_two}')

cities("Nairobi", "Dar es Salaam")


# General purpose decorators with args and kwargs

def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args,**kwargs):
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
        function_to_decorate(*args)
    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("No arguments here.")

function_with_no_argument()


@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print(a, b, c)

function_with_arguments(1, 2, 3)


@a_decorator_passing_arbitrary_arguments
def function_with_keyword_arguments():
    print("This has shown keyword arguments")

function_with_keyword_arguments(first_name="Ben", last_name="Solo")


# Passing Arguments to the Decorator
import functools

def decorator_maker_with_arguments(decorator_arg1, decorator_arg2, decorator_arg3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(function_arg1, function_arg2, function_arg3) :
            "This is the wrapper function"
            print("The wrapper can access all the variables\n"
                  "\t- from the decorator maker: {0} {1} {2}\n"
                  "\t- from the function call: {3} {4} {5}\n"
                  "and pass them to the decorated function"
                  .format(decorator_arg1, decorator_arg2,decorator_arg3,
                          function_arg1, function_arg2,function_arg3))
            return func(function_arg1, function_arg2,function_arg3)

        return wrapper

    return decorator

pandas = "Pandas"

@decorator_maker_with_arguments(pandas, "Numpy","Scikit-learn")
def decorated_function_with_arguments(arg1, arg2, arg3):
    """This has a decorator that accepts arguments"""
    print("This is the decorated function and it only knows about its arguments: {0}"
           " {1}" " {2}".format(arg1, arg2, arg3))

decorated_function_with_arguments(pandas, "Science", "Tools")

print(decorated_function_with_arguments.__name__)
print(decorated_function_with_arguments.__doc__)
