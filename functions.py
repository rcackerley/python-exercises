def sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

#print sum([1, 2, 3])

def largest(numbers):
    biggest = 0
    for number in numbers:
        if number > biggest:
            biggest = number
    return biggest

#print (largest([1, 5, 11]))


def smallest(numbers):
    tinyiest = numbers[0]
    for number in numbers:
        if number < tinyiest:
            tinyiest = number
    return tinyiest

#print (smallest([1, 5, 11, -20]))

def even_numbers(numbers):
    my_even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            my_even_numbers.append(number)
    return my_even_numbers

#print even_numbers([20, 17, 3, 4])

def positive_numbers(numbers):
    positives = []
    for number in numbers:
        if number > 0:
            positives.append(number)
    return positives

#print positive_numbers([-1, 2, 3, -44])

def multiplied(numbers, factor):
    product = []
    for number in numbers:
        product.append(number * factor)
    return product

#print multiplied([1, 2, 3, 4, 5], 9)

def pair_mulitplier(nums1, nums2):
    nums_new = []
    for i in range(len(nums1)):
        nums_new.append(nums1[i] * nums2[i])
    return nums_new
#print pair_mulitplier([1, 2, 3, 4], [9, 8, 7, 6])


a = [
    [1, 2],
    [2, 3],
]
b = [
    [4, 5],
    [6, 7],
]

# def adding_matrix(matrix1, matrix2):

#     matrix3 = [
#         [None, None],
#         [None, None],
#     ]
    
#     for i in range(len(matrix1)):
#         for j in range(len(matrix1[i])):
#             matrix3[i][j] = matrix1[i][j] + matrix2[i][j]
#     return matrix3
            
# print adding_matrix(a, b)

def create_a_matrix(matrix1, matrix2):
    row = len(matrix1)
    column = len(matrix2)

    matrix3 = row * [(column * [0])]
    matrix3[0][0] = 5
    print matrix3
    return matrix3

def adding_matrix(matrix1, matrix2):
    matrix3 = create_a_matrix(matrix1, matrix2)
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            matrix3[i][j] = matrix1[i][j] + matrix2[i][j]
            #print i
            #print j
            # print matrix1
            # print matrix2
            #print matrix3[i][j]
            #print matrix1[i][j] + matrix2[i][j]
            #print matrix3
    return matrix3

adding_matrix(a, b)

