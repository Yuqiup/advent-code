#!/usr/bin/env python3
import re
import numpy as np

with open("data2", "r") as file:
    # r g b
    thresh = [12, 13, 14]

    s = 0
    result = 0
    for line in file:
        s += 1
        print(line)
        color = ["red", "green", "blue"]

        string = line.split(":")[-1]
        string = string.replace(",", "")
        print(string)
        valid = True
        min_vec = [0, 0, 0]
        for set in string.split(";"):
            value = [0, 0, 0]
            temp_n = 0
            set = set.strip()
            for ss in set.split(" "):
                # print(ss)
                if ss.isdigit():
                    temp_n = int(ss)
                if "red" in ss:
                    value[0] += int(temp_n)
                if "green" in ss:
                    value[1] += int(temp_n)
                if "blue" in ss:
                    value[2] += int(temp_n)
            print(value)
            min_vec = np.maximum(value, min_vec)
            # print(min_vec)
        result += np.prod(min_vec)

print(result)
