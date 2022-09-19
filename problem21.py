# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called
# amicable numbers. For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
# therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.

total = 0
for number_1 in range(2, 10000):  # testing numbers from 2 to 10,000
    sum_number_1 = 0
    
    # find sum of divisors of number_1
    for x in range(1, number_1):
        if number_1 % x == 0:
            sum_number_1 += x
    sum_number_2 = 0

    # find sum of divisors of number_2
    number_2 = sum_number_1
    for x in range(1, number_2):
        if number_2 % x == 0:
            sum_number_2 += x

    # if number_1 and number_2 are a amicable number pair, then save
    if sum_number_2 == number_1 and number_1 != number_2:
        print('pair found', number_1, number_2)
        total += (number_1 + number_2) / 2  # taking the average takes into account the pair occurs twice

# print result
print('sum of amicable pairs less than 1000 is', int(total))
