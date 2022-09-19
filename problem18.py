# Problem 18: Maximum path sum I
# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total
# from top to bottom is 23.
#     3
#    7 4
#   2 4 6
#  8 5 9 3
# That is, 3 + 7 + 4 + 9 = 23. Find the maximum total from top to bottom of the triangle below:

A = [75, 95, 64, 17, 47, 82, 18, 35, 87, 10, 20, 4, 82, 47, 65, 19, 1, 23, 75, 3, 34, 88, 2, 77, 73, 7, 63, 67, 99, 65,
     4, 28, 6, 16, 70, 92, 41, 41, 26, 56, 83, 40, 80, 70, 33, 41, 48, 72, 33, 47, 32, 37, 16, 94, 29, 53, 71, 44, 65,
     25, 43, 91, 52, 97, 51, 14, 70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57, 91, 71, 52, 38, 17, 14, 91, 43, 58, 50,
     27, 29, 48, 63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31, 4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53,
     60, 4, 23]
height_width = 15

# creating lists with arrays nested
list_A = []
for i in range(height_width):
    start_i = sum(range(i + 1))  # found index values for start and end of each array
    end_i = sum(range(i + 2)) - 1
    array_temp = A[start_i:end_i + 1]  # find array and saving to list
    # print('start', start_i, ' end index', end_i, array_temp)
    list_A.append(array_temp)
# print(list_A)  # print entire list of arrays

# for j in reversed(range(height_width)):
for j in reversed(range(1, height_width)):
    upper = list_A[j - 1]  # upper and lower arrays
    lower = list_A[j]
    # print(upper, lower)
    list_B = []
    for i in range(len(upper)):
        if lower[i] > lower[i + 1]:
            upper[i] = upper[i] + lower[i]
        else:
            upper[i] = upper[i] + lower[i + 1]
        # print(upper[i])
        list_B.append(upper[i])
    print(list_B)
