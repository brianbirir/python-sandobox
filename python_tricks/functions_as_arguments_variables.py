'''
functions as:

1. Arguments for other functions
2. Values returned from other functions
3. assigned variables that can be stored in data structures

'''


def myfunc(a, b):
	return a+b


# list data structure
funcs = [myfunc]
funcs[0]

print(funcs[0](2, 3))
