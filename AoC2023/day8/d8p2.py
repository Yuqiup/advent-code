import re
import math as ms
from functools import reduce


class node_map:
    def __init__(self, ls_node, start):
        # build dicts
        key_sym = []
        left_sym = []
        right_sym = []

        for i in range(0, len(ls_node), 3):
            key_sym.append(ls_node[i])
            left_sym.append(ls_node[i + 1])
            right_sym.append(ls_node[i + 2])
        self.l_map = dict(zip(key_sym, left_sym))
        self.r_map = dict(zip(key_sym, right_sym))

        self.cur = start
        # self.goal = goal
        self.ct = 0
        self.period = []
        self.Done = False

    def step(self, direction):
        if self.Done:
            return True
        self.ct += 1

        if direction:
            self.cur = self.l_map[self.cur]
        else:
            self.cur = self.r_map[self.cur]
        # print(f"Dir: {direction} -> {self.cur}")
        if self.cur.endswith("Z"):
            if self.ct not in self.period:
                self.period.append(self.ct)
                self.ct = 0
                return False
            else:
                self.Done = True
                return True

        else:
            return False


with open("data2", "r") as file:
    inst_seq = file.readline().strip()
    data = file.read().strip()

inst_seq = [c == "L" for c in inst_seq]
ls_node = re.findall(r"(\w+)", data)

start_node = []
for i in range(0, len(ls_node), 3):
    if ls_node[i].endswith("A"):
        start_node.append(ls_node[i])

N_ghosts = len(start_node)
sol = [node_map(ls_node, start_node[i]) for i in range(N_ghosts)]
goal = [False] * N_ghosts

iter = 0
while not all(goal):
    if iter == 1e6:
        break
    for d in inst_seq:
        iter += 1

        # goal = [sol[i].step(d) for i in range(N_ghosts)]
        for i, o in enumerate(sol):
            goal[i] = o.step(d)

        if all(goal):
            break
            print(f"{iter}: {[o.cur for o in sol]}")


theta = [o.period[-1] for o in sol]
min_step = reduce(ms.lcm, theta)

print(f"min steps: {min_step}")
