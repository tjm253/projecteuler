# Problem 22: Names scores
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand
# first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each
# name, multiply this value by its alphabetical position in the list to obtain a name score.
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
# is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
# What is the total of all the name scores in the file?

print('importing to line of text...')
with open('p022_names.txt') as f:
    lines = f.readlines()
print(lines)
lst = []
flag_1 = False
flag_2 = False

print('saving to list...')
# searches for 1st and second double quote which is then used to find word
for x in range(len(lines[0])):
    if lines[0][x] == '\"' and not flag_1:
        flag_1 = True
        start = x
    if flag_1 and start < x and lines[0][x] == '\"':
        flag_2 = True
        end = x
    if flag_1 and flag_2:
        lst.append(lines[0][start+1:end])
        flag_1 = False
        flag_2 = False

print(lst)
print('sorting alphabetically...')
lst.sort()
print(lst)

# x is the alphabetical position of the name
cumul = 0
for x in range(len(lst)):

    # find the sum of the ascii characters (note that it only works for uppercase inputs)
    ascii_sum = 0
    for y in range(len(lst[x])):
        ascii_sum += ord(lst[x][y]) - 64
    cumul += ascii_sum * (x + 1)  # add to the running sum of the ascii sum * x-position of the name

print('answer:', cumul)
