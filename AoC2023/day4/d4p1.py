#!/usr/bin/env python3

with open('data1', 'r') as file:
    lines = file.readlines()

lines = [line.strip('\n').split(':')[1] for line in lines]

total = 0
for line in lines:
    tmp = line.split('|')
    win_num = tmp[0].strip().split()
    my_num = tmp[1].strip().split()
    print(win_num)
    print(my_num)
    print('-------------------')
    score = 0
    for num in my_num:
        if num in win_num:
            if score == 0:
                score = 1
            else:
                score *= 2
    print(score)
    total += score
print(f"total: {total}")
