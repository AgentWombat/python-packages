# The "as np" clause after the import statement changes
# the name we will use to reference numpy throughout our code.
# So, instead of having to type "numpy.FUNCTION", we now type "np.FUNCTION"
import numpy as np

# Numpy arrays are superior to default Python lists for machine learning
# purposes.

# To create a numpy array, supply an array into the below function.
array = np.array([3.14, 1.618, 2.71828])

print(array)

# Numpy arrays function very similarly to normal Python lists.
# The main difference is Numpy arrays cannot be appended--
# that is, there is no "array.append()"

print("The first element of the array is", array[0])
print("The last element of the array is", array[-1])

print("Here are all of the elements in the array:")
for number in array:
	print(number)


# A 2D array can be created like so:

array_2d = np.array([[3.14, 1.618, 2.71828], [115, 935, 4]])

print(array_2d)

# To create a numpy array with a certain size, we can use "np.zeros" or "np.ones"
# "shape" determines the dimensions of the array
zeros = np.zeros(shape = (2,5))
print(zeros)

ones = np.ones(shape = (7,2))
print(ones)

# A big plus for Numpy arrays is the ability to run numerical operations theron.
# All operations are applied between two arrays use corresponding elements
# to determine the output.
print("--ARRAY ARITHMETIC--")
array1 = np.array([1,2,3])
array2 = np.array([5,9,2])

print("array1 =", array1)
print("array2 =", array2)
print("array1 + 4 =", array1 + 4)
print("array1 / 2 =", array1 / 2)
print("array1^4 =", array1 ** 4)
print("array1 + array2 =", array1 + array2)
print("array1 / array2 =", array1 / array2)
print("array1^array2 =", array1 ** array2)



