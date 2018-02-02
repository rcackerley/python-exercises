star = '*'
space = ' '
num_of_stars = 1
num_of_spaces = 6
for row in range (0, 4):
    print ((num_of_spaces / 2)  * space) + (star * num_of_stars) + ((num_of_spaces / 2)  * space)
    num_of_stars = num_of_stars + 2
    num_of_spaces = num_of_spaces - 2

