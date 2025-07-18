# What is Numpy?
- NumPy is a Python library used for working with arrays.
- The array object in numpy is called `ndarray`. We can create `ndarray` object by `array()`
```python
import numpy as np 

my_list = [1,2,3]

my_matrix = [[1,2,3],[4,5,6],[7,8,9]]

arr = np.array(my_list)
arr_2d = np.array(my_matrix)

print(arr)
# [1 2 3 ]
print(arr_2d)
# [[1 2 3] 
#  [4 5 6] 
#  [7 8 9]]
```

# Built-in Methodes
## arange
```python
np.arange(0,10)
#[0 1 2 3 4 5 6 7 8 9]
np.arange(0,11,2)
#[0 2 4 6 8 10]
```
## zeros and ones
```python
print(np.zeros(3))
#[0. 0. 0.] all of them is float 
print(np.ones((3,3)))
# [[1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]]
```
## linspace
