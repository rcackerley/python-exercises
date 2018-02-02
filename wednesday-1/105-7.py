star = '*'
height_of_square = int(raw_input('What is the height the square?'))
width_of_the_square = int(raw_input('What is the width of the square?'))
for row in range(0,height_of_square):
    if row == 0 or row == height_of_square - 1:
        print star * width_of_the_square
    else:
        inside_of_box = width_of_the_square - 2
        print star + (' ' * inside_of_box) + star
        