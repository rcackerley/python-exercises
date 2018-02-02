def matrix(Matrix_1,Matrix_2):
   height = len(Matrix_1)
   width = len(Matrix_1[0])

   result = []

   for i in range(0, height):
       result.append([])
       for j in range(0, width):
           result[i].append(None)

   for i in range(0, height):
       for j in range(0, width):
           cell1 = Matrix_1[i][j]
           cell2 = Matrix_2[i][j]

           result[i][j] = cell1 + cell2
   return result
print (matrix([[2, -2],[5, 3]],[[4, 3],[-3, 1]])) 

Matrix_1 = [
   [2, -2],
   [5, 3]
]
Matrix_2 = [
   [4, 3],
   [-3, 1]
]