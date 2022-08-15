# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

limit = 20
product = 1
list_prime = []
# find all prime values
for x in range(2, 21):
    for i in range(2, x):
        if (x % i) == 0:
            print(x, "is not a prime number")
            break
    else:
        print(x, "is a prime number")
        list_prime.append(x)
# find what max power that each prime value shows up
power = []
for j in range(len(list_prime)):
    power_test = 0
    # break when the evaluated power is more than limit
    for nth_root in range(1, 21):
        t = list_prime[j]**nth_root
        if t > limit:
            power.append(power_test)
            break
        else:
            power_test += 1
# find the product of the evaluated largest multiples
for i in range(len(power)):
    product = product*(list_prime[i] ** power[i])
print('the number of primes found is', len(power), 'and are', list_prime)
print('the largest powers found', power)
print('the product is', product)
