'''
Pass Statement

Disregard a condition and continue to run the program as usual
'''
number = 0 

for number in range(10):
    number = number + 1

    if number == 5:
        pass

    print('Number is ' + str(number))
print('Out of loop!')