string = raw_input('Text?')

width = len(string) + 2
num_of_blanks = width - 2

print '*' * width
print '*' + string + '*'
print '*' * width
