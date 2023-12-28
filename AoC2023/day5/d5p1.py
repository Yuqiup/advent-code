import numpy as np

class range_map:
    def __init__(self, dst, src, length):
        self.src = src
        self.dst = dst
        self.length = length

    def map(self, val):
        dif = val - self.src
        if dif < 0:
            return val, False
        if dif >= self.length:
            return val, False
        return self.dst + dif, True


seed2soil = range_map(50,98,2)
print(seed2soil.map(51))


with open('data1', 'r') as file:
    lines = file.readlines()

seeds = lines[0].split(':')[1].strip().split(' ')
seeds = [int(s) for s in seeds]
print(seeds)

for line in lines:
    if not line[0].isdigit():
        hit_flg = [False] * len(seeds)
        print(line)
        continue

    ran = line.strip().split(' ')
    map = range_map(int(ran[0]), int(ran[1]), int(ran[2]))
    for i in range(len(seeds)):
        if not hit_flg[i]:
            seeds[i], hit_flg[i] = map.map(seeds[i])

    print(seeds)

print(min(seeds))
