'''
Break statement

Exit out of a loop when an external condition is triggered
'''

number = 0 

for number in range(10):
    number = number + 1

    if number == 5:
        break

    print('Number is ' + str(number))
print('Out of loop!')