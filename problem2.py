# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
limit = 4000000
x = 1
y = 1
sum = 0
print(x)
while x < limit and y < limit:
    x += y
    y += x
    print(x,y)
    if x < limit and x % 2 == 0:
        sum = x + sum
        print(x)
    if y < limit and y % 2 == 0:
        sum = y + sum
        print(y)
print('sum:',sum)