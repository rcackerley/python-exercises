star = '*'
space = ' '
num_of_stars = 1
height = int(raw_input('Whats the height?'))
width = 1
for number in range(0, height):
    width = width + 2 
    print width
width = width - 2
num_of_spaces = height - 1
for row in range (0, height):
    print ((width / 2)  * space) + (star * num_of_stars) + ((width / 2)  * space)
    num_of_stars = num_of_stars + 2
    width = width - 2

