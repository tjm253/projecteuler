# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
z = 0
count = 0
for j in reversed(range(1,1000)):
    for i in reversed(range(1,1000)):
        x = i*j
        string = str(x)
        string_rev = string[::-1]
        x_rev = int(string_rev)
        # print(x,string,x_rev,string_rev)
        if x/x_rev == 1:
            break
    # print(x)
    if x > z:
        z = x
    count += 1

print(z)