#!/usr/bin/env python3
import re


def cov2num(text):
    digit_map = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    buffer = "     "
    str_out = ""
    for s in text:
        if s.isdigit():
            str_out += s
        else:
            buffer += s
            n = 0
            for i in range(len(digit_map)):
                if digit_map[i] in buffer:
                    buffer = "   " + buffer[-2] + buffer[-1]
                    str_out += str(i)
                    break
                else:
                    n += 1
    return str_out


filename = "datain2"
with open(filename, "r") as file:
    s = 0
    for line in file:
        line = cov2num(line)
        print(line)
        match = re.findall(r"\d", line)
        print(match)
        if len(match) > 1:
            s += int(match[0] + match[-1])
        elif len(match) == 1:
            s += int(match[0] + match[0])

print(s)
