# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the
# 6th prime is 13. What is the 10001st prime number?

count = 0
limit = 10001  # nth prime

limit = limit-1
for num in range(1, 1000000000000):
    num = num * 2 + 1
    # If given number is greater than 1
    if num > 1:

        # Iterate from 2 to n / 2
        for i in range(2, int(num / 2) + 1):

            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                # print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
            prime = num
            count += 1
    # else:
        # print(num, "is not a prime number")
    if count == limit:
        print('break, that is', count+1, 'primes')
        break
print('the answer is', num)
