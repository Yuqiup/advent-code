#!/usr/bin/env python3
import re


filename = "datain1"

with open(filename, "r") as file:
    s = 0
    for line in file:
        match = re.findall(r"\d", line)
        print(match)
        if len(match) > 1:
            s += int(match[0] + match[-1])
        elif len(match) == 1:
            s += int(match[0] + match[0])


print(s)
