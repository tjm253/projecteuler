# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th
# triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# Let us list the factors of the first seven triangle numbers:
#    1: 1
#    3: 1,3
#    6: 1,2,3,6
#    10: 1,2,5,10
#    15: 1,3,5,15
#    21: 1,3,7,21
#    28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over five hundred divisors?

# number of wanted divisors
divisors = 5
# number of terms
limit = 10
# pre-allocations
x = 0
# find the triangle numbers on by one
for i in range(1, limit+1):
    y = x + i
    print(x, '+', i, '=', y)
    x = y

# the next step is to import prime numbers and count the number of times a prime is factored out
# if the number is 40, then divide out 2, then 2, then 2, then 5 is left over
# and counting 1 and 40, that is 6 divisors.