# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
import time

start_time = time.perf_counter() # or time.perf_counter_ns()
# given non-inclusive limit for prime numbers (number must be 12 or larger)
limit = 2000000

# initial values and pre-allocations
primes = [2, 3, 5, 7]
prime_sum = 17

# testing all odd numbers
for num in range(4, 1000000000):
    num = 2 * num + 1

    # test if number is above given limit
    if num >= limit:
        print('broke at', num, 'and was not accounted for')
        break

    # you don't have to test the number 2 since we only have to test odd numbers
    # anything bigger than the square of the number is impossible to occur
    # find where the previous prime values cross sqrt(num)
    start = 1
    stop_value = int((primes[-1]) ** (1 / 2)) + 1  # using power is close to numpy.sqrt() speed
    stop = 0
    for j in primes:
        stop = stop + 1
        if stop_value < j:
            stop = stop + 1  # just to be safe
            # break out of loop when index of sqrt(prime) is found
            break

    # define/reset flag
    flag = True
    # check for from previous prime factors
    for i in primes[start:stop]:
        if (num % i) == 0:
            # if factor is found to be not prime, set flag to False
            flag = False
            # break out of loop
            break

    # check if flag is True (number is prime)
    if flag:
        # add new prime to prime list, add prime to sum of primes
        # and display results (prime, prime sum, and stop index)
        primes.append(num)
        prime_sum += num
        print(num, "is a prime number", '| and the prime sum is', prime_sum, '| stop index examined up to', stop)

end_time = time.perf_counter()  # or time.perf_counter_ns()
print(end_time - start_time)
