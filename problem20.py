# Problem 20: Factorial digit sum
# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!

limit = 100
y = 1
total = 0

for i in (range(1, limit+1)): # compute factorial using for loop
    y = i * y
print(limit, 'factorial is', y)

y_str = str(y)  # convert to string
for x in range(len(y_str)):  # select index of string -> integer, and then add to find sum of digits
    total += int(y_str[x])

print('the sum of the digits is:')
print(total)
