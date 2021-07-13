# We can get new functions in our code by using import statements
# Python has many built in packages and libraries. I have highlighted
# two here that I find particularly usefull.
# Typically, all import statements are placed at the top of a Python script;
# however, for purposes of covering one at a time, I will break this convention
import math # This contains a slew a mathematical functions and constants
print("--MATH--")
print("The square root of 144 is", math.sqrt(144))
print("The sin of pi/6 is", math.sin(math.pi / 6))
print("The base of the natural logarithm (e) equals", math.e)
# There are many more math functions available

import random # This contains functions for generating random numbers
print("--RANDOM--")
# This will print a random number from the set of integers on [0,100)--
# that is the numbers {0, 1, 2, 3, 4... 97, 98, 99}
print(random.randrange(0,100))

# To make the "randomness" consistant, which is usefull for debugging, you can set a seed.
random.seed(14)
print("This will always print the same sequence. (run script multiple times)")

# The function "range(H)" generates an arrangement of integers
# from 0 to the number H (but not including H). It is very usefull for for-loops.
# The effect here is to run the print statement 10 times
for i in range(10):
	print(random.randrange(0,10))

