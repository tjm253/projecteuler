# The sum of the squares of the first ten natural numbers is,
# The square of the sum of the first ten natural numbers is,
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is. Find the difference between the sum of
# the squares of the first one hundred natural numbers and the square of the sum.

k = 100
n = 0
N = 0
for x in range(1, k+1):
    n = n + x**2
    N = N + x
N = N**2
print('N is', N, 'n is', n)
print('the answer is:',N-n)
