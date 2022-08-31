# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)       n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.


count_record = 1
start_list = [2]
count_list = [1]
# we will be examining numbers from 2 to two-million
for start in range(3,10):
    num = start
    count = 0
    
    # this loop continues until the number reaches 1
    for i in range(100):
        # print('num is', num)
        flag = False
        for j in range(len(start_list)):
            if int(num / start_list[j]) == 1:
                # print(start_list[j], 'was previously found')
                num = start_list[j]
                count = count + count_list[j]
                flag = True
                break
        if flag:
            break
        if num % 2 == 0:
            num = int(num/2)
            count += 1
        elif num == 1:
            break
        else:
            count += 1
            num = 3*num + 1
        start_list.append(start)
        count_list.append(count)
    if count_record < count:
        count_record = count
        print(start, 'took', count, 'operations to get to 1')


    
    
