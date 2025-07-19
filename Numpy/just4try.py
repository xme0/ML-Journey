import numpy as np 

my_list = [1,2,3]

my_matrix = [[1,2,3],[4,5,6],[7,8,9]]

arr = np.array(my_list)
arr_2d = np.array(my_matrix)

print(arr)
# [1 2 3 ]
print(np.zeros(3))
# [[1 2 3] 
#  [4 5 6] 
#  [7 8 9]]

print(np.ones((3,3)))

# [[1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]]