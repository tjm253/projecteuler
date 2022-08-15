# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?
x = 600851475143
y = x
# i tests each value repeatedly until it has been fully deprived
for i in range(2, y-1):
    remainder = x % i
    # if remainder == 0:
    while remainder == 0:
        x = x/i
        j = i
        remainder = x % i
        print(j)
    if i > x:
        break
