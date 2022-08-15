# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

limit = 1000
# in python, there is no option to break out of nested loop: flag method is used here
flag_break = False
# specify first and second term test
for x in range(1, limit):
    for y in range(x + 1, limit):
        # since sum of x,y and z is 1000, z can be found from x and y
        z = limit - x - y
        # make sure not to analyze z values less than y
        if z < 0 or z <= y:
            break
        # find the squared value
        B = x ** 2 + y ** 2
        print('x,y,z', x, y, z)
        # see if it is a perfect square, break both loops if true
        if B == z ** 2:
            flag_break = True
            break
    if flag_break:
        break
# print results
print(x, '+', y, '+', z, '=', 1000)
print('product of x, y and z is', x * y * z)
