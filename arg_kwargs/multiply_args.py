def multiply(x, y):
    print (x * y)


multiply(5, 4)


def multiply_args(*args):
    z = 1
    for num in args:
        z *= num
    print(z)


multiply_args(4, 5)
multiply_args(10, 9)
multiply_args(2, 3, 4)
multiply_args(3, 5, 10, 6)
