first_number = 1
second_number = 1

for i in range (0,10):
    for ii in range (0,10):
        print '%s * %s = %s' % (first_number, second_number, (first_number * second_number))
        second_number += 1
    second_number = 1
    first_number += 1