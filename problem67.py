# Problem 67: Maximum path sum II
# By starting at the top of the triangle below and moving to adjacent numbers on the row below,
# the maximum total from top to bottom is 23.
#    3
#   7 4
#  2 4 6
# 8 5 9 3
# That is, 3 + 7 + 4 + 9 = 23. Find the maximum total from top to bottom in triangle.txt
# (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

import time

st = time.time()  # start timer

# open the text document (note that it has line breaks as \n)
with open('p067_triangle.txt') as f:
    lines = f.readlines()
# print(lines)
dim = len(lines)  # dim = 100

# find the rows of the triangle as a list of arrays
list_A = []
for j in range(0, dim):  # substring indexing
    list_B = []
    for i in range(0, j+1):  # sub-substring indexing
        # find start/end within substring or the index of the sub-substring
        # [s.str,s.s.str] = [0, {0,1}], [1, {0,1,3,4}], [2, {0,1,3,4,6,7}],...
        start = i * 3
        end = start + 1
        string_temp = lines[j][start:end+1]
        # print('substring', j, 'start', start, 'end', end, 'string_temp', string_temp)
        list_B.append(int(string_temp))
    # print(list_B)
    list_A.append(list_B)  # append found row values to the triangle list
print(list_A)  # print data

# find the highest pair starting from the bottom the triangle and then add together to make new bottom row
for j in reversed(range(1, dim)):
    upper = list_A[j - 1]  # upper and lower arrays
    lower = list_A[j]
    # print(upper, lower)
    list_B = []
    for i in range(len(upper)):
        if lower[i] > lower[i + 1]:  # if pair is higher than the other, add together to make new value in array
            upper[i] = upper[i] + lower[i]
        else:
            upper[i] = upper[i] + lower[i + 1]
        # print(upper[i])
        list_B.append(upper[i])
    print(list_B)  # print final value

et = time.time()  # end timer
print('Execution time:', et - st, 'seconds')