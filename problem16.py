# Problem 16: Power digit sum
# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 21000?

# Python makes it easy to calculate the value of 2^1000 and handles large int easily
A = 2 ** 1000
print(A)
# turn into string so that we can easily index the values
A_str = str(A)
print(A_str)
x = 0
# from the first digit to the last, finding the sum
for i in range(len(A_str)):
    x += int(A_str[i])
    # print(x)
# print the answer
print('the answer is', x)
