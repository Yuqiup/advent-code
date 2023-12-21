#!/usr/bin/env python3
import numpy as np

def win_num_count(line):

    tmp = line.split('|')
    win_num = tmp[0].strip().split()
    my_num = tmp[1].strip().split()
    print(win_num)
    print(my_num)
    print('-------------------')
    score = 0
    for num in my_num:
        if num in win_num:
            score += 1
            print(f"win count:{score}")

    return score

with open('data2', 'r') as file:
    lines = file.readlines()

lines = [line.strip('\n').split(':')[1] for line in lines]
totoal = 0

copies = np.ones(len(lines))
for i in range(len(lines)):
    win_counts = win_num_count(lines[i])
    for win_idx_diff in range(win_counts):
        idx = i + win_idx_diff + 1
        if idx < len(lines):
            copies[idx] += copies[i]

print(f"total: {sum(copies)}")
