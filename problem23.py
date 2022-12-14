# Problem 23: Non-abundant sums
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example,
# the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number. A
# number n is called deficient if the sum of its proper divisors is less than n, and it is called abundant if this sum
# exceeds n. As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written
# as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than
# 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by
# analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant
# numbers is less than this limit. Find the sum of all the positive integers which cannot be written as the sum of
# two abundant numbers.

start = 12
end = 128123


def is_abundant(n):
    sum_of_divisors = 1
    for x in range(2, n // 2 + 1):  # find the divisors of x
        if n % x == 0:
            sum_of_divisors += x
    return sum_of_divisors > n


for z in range(12, 28124):
    if is_abundant(z):
        print(z, 'is abundant')


# list of abundant numbers - the smallest abdundant no is 12
abundantNums = [number*3 for number in range(12,28124) if is_abundant(number)]
print(abundantNums)