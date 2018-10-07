# source: realpython.com

# swap the values of a and b

a = 23
b = 42


# classic method
tmp = a
a = b
b = tmp

# new method
a, b = b, a