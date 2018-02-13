'''
Continue Statement

Skip over a part of a loop where an external condition is triggered
'''

number = 0 

for number in range(10):
    number = number + 1

    if number == 5:
        continue

    print('Number is ' + str(number))
print('Out of loop!')