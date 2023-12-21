import numpy as np

class range_map:
    def __init__(self):
        self.src = []
        self.dst = []
        self.length = []

    def append_map(self, dst, src, length):
        self.src.append(src)
        self.dst.append(dst)
        self.length.append(length)

    def map_pair(self, src_start, src_end, map_start, map_end, dst_start, dst_end):
        mapped_list = []
        unmaped_list = []
        # print(src_start, src_end, map_start, map_end, dst_start, dst_end)
        if src_end < map_start:
            unmaped_list.append([src_start, src_end])
            # print("U1")
            return mapped_list, unmaped_list

        if src_start > map_end:
            unmaped_list.append([src_start, src_end])
            # print("U2")
            return mapped_list, unmaped_list

        if src_start < map_start:
            unmaped_list.append([src_start, map_start - 1])

        if src_end > map_end:
            unmaped_list.append([map_end + 1, src_end])

        if src_start >= map_start:
            o_start = dst_start + (src_start - map_start)
        else:
            o_start = dst_start

        if src_end <= map_end:
            o_end = dst_start + (src_end - map_start)
        else:
            o_end = dst_end

        # print("M")
        mapped_list.append([o_start, o_end])
        return mapped_list, unmaped_list


    def map(self, in_list):
        ls_ump = in_list
        # print(in_list)
        temp_list = in_list
        ls_map = []
        for i in range(len(self.src)):
            if i > 0:
                ls_ump = temp_list
            temp_list = []
            map_start = self.src[i]
            map_end = self.src[i] + self.length[i] - 1
            dst_start = self.dst[i]
            dst_end = self.dst[i] + self.length[i] - 1
            # print(i)
            # print(f"inter{ls_ump}")
            for ump_pair in ls_ump:
                mapped_list, unmaped_list = self.map_pair(
                    ump_pair[0], ump_pair[1],
                    map_start, map_end,
                    dst_start, dst_end,
                )
                # print(unmaped_list)
                ls_map += mapped_list
                temp_list += unmaped_list
                # print(f"mapped{mapped_list}")
                # print(f"temp{temp_list}")

        if temp_list:
            return ls_map + temp_list
        else:
            return ls_map


with open('data2', 'r') as file:
    lines = file.readlines()

seeds_pair = lines[0].split(':')[1].strip().split(' ')
seeds_pair = [int(s) for s in seeds_pair]

seeds = []
for i in range(0, len(seeds_pair), 2):
    seeds.append([seeds_pair[i], seeds_pair[i] + seeds_pair[i+1] - 1])

line_map = range_map()
for line in lines:
    if not line[0].isdigit():
        if line[0] == '\n':
            continue

        seeds = line_map.map(seeds)
        print('-------------------')
        print(line_map.src)
        print(line_map.dst)
        print(line_map.length)
        print('-------------------')
        print(seeds)
        print('-------------------')
        print(line)
        line_map = range_map()
        continue

    ran = line.strip().split(' ')
    line_map.append_map(int(ran[0]), int(ran[1]), int(ran[2]))

    # print(seeds)
seeds = line_map.map(seeds)

min_seeds = min([s[0] for s in seeds])
print(f"final loc: {seeds}")

print(f"min: {min_seeds}")
