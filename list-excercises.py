#print the sum of all numbers in a list

# list_of_numbers = [1, 2, 3, 4, 5, 6, 7]
# sum_of_numbers = 0
# for number in list_of_numbers:
#     sum_of_numbers = sum_of_numbers + number
#     #print sum_of_numbers
# print sum_of_numbers
    



#print the largest number in a list
# list_of_numbers = [22, 12, 883, 34, 65, 98, 127]
# sorted_list = sorted(list_of_numbers, reverse=True)
# print sorted_list[0]

#print the smallest number in a list
# list_of_numbers = [22, 12, 883, 34, 65, 98, 127]
# sorted_list = sorted(list_of_numbers)
# print sorted_list[0]


#print the even numbers
# list_of_numbers = [22, 12, 883, 34, 65, 98, 127]
# even_numbers = []
# for number in list_of_numbers:
#     if number % 2 == 0:
#         even_numbers.append(number)

# print even_numbers


#print the positive numbers & positive numbers II
# list_of_numbers = [22, -12, 883, 34, -65, 98, 127]
# positive_numbers = []
# for number in list_of_numbers:
#     if number >= 0:
#         positive_numbers.append(number)

# print positive_numbers


# Mulitply a List
# list_of_numbers = [1, 2, 3, 5, 8, 99]
# factor = 8
# products_of_multiplication = []
# for number in list_of_numbers:
#     products_of_multiplication.append(number * factor)

# print products_of_multiplication


#Multiply Vectors
# list1 = [2, 7, 8]
# list2 = [1, 8, 9]
# result_list = []
# for number in range(len(list1)):
#     result_list.append(list1[number] * list2[number])
# print result_list



# #Matrix Addition
# list_of_lists1 = [
#     [8, 6],
#     [4, 8]
# ]

# list_of_lists2 = [
#     [3, 9],
#     [2, 4]
# ]

# product_lists_inner = []

# for array in range(0, len(list_of_lists1)):
#     for inner_array in range(0,2):
#         #print list_of_lists1[array][inner_array]
#         product_lists_inner.append(list_of_lists1[array][inner_array] * list_of_lists2[array][inner_array])

# print product_lists_inner


#Matrix Addition Part 2
list_of_lists1 = [
    [8, 6],
    [4, 8],
    [9, 5],
]

list_of_lists2 = [
    [3, 9],
    [2, 4],
    [6, 6],
]

product_lists_inner = []

for array in range(0, len(list_of_lists1)):
    for inner_array in range(0, len(list_of_lists1[0])):
        #print list_of_lists1[array][inner_array]
        product_lists_inner.append(list_of_lists1[array][inner_array] + list_of_lists2[array][inner_array])

print product_lists_inner


# de-dup
# duplicated_list = [9, 9, 8, 8, 7, 7, 7]
# no_dup_list = []

# for item in range(0, len(duplicated_list)):
#     if duplicated_list[item] not in no_dup_list:
#         no_dup_list.append(duplicated_list[item])
# print no_dup_list


#bonus matrix challenge
# matrix1 = [
#     [2, 2],
#     [3, 3],
# ]

# matrix2 = [
#     [1, 1],
#     [4, 4]
# ]

# new_matrix = [
#     [],
#     []
# ]
# t = 0
# for i in matrix1:
#    for x in matrix1[t - 1]:
#        print x
#        t += 1
