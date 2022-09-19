# Problem 17: Number letter counts
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 +
# 5 + 4 + 4 = 19 letters used in total. If all the numbers from 1 to 1000 (one thousand) inclusive were written
# out in words, how many letters would be used?
# Note: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and
# 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in
# compliance with British usage.


# Number letter counts

n1 = (0, 3, 3, 5, 4, 4, 3, 5, 5, 4)  # 1 to 9
n10 = (0, 3, 6, 6, 5, 5, 5, 7, 6, 6)  # 10 to 90
n11 = (0, 6, 6, 8, 8, 7, 7, 9, 8, 8)  # 11 to 19
n = (7, 10, 11)  # hundred, hundred and, one thousand

n1to99x10 = (sum(n1) * 9 + n10[1] + sum(n11) + sum(n10[2:]) * 10) * 10  # from 1 to 99 all
n100to900all = n[0] * 9 + n[1] * 99 * 9 + sum(n1) * 100  # from 100 to 900

letters = n1to99x10 + n100to900all + n[2]
print(letters)  # 21124

