starting_number = int(raw_input("What number do you want to start with?"))
ending_number = int(raw_input("What number do you want to end with?"))
ending_number += 1

if starting_number >= ending_number:
    print "Hey! Make the starting number less than the ending number"
else:
    my_number_array = range(starting_number, ending_number)
    for number in my_number_array:
        print number