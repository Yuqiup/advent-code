import re


class d8p1:
    def __init__(self, data, start, goal):
        # build dicts
        ls_node = re.findall(r"(\w+)", data)

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
        self.goal = goal
        self.ct = 0

    def step(self, seq):
        for direction in seq:
            self.ct += 1

            if direction == "L":
                self.cur = self.l_map[self.cur]
            else:
                self.cur = self.r_map[self.cur]

            print(f"Dir: {direction} -> {self.cur}")
        if self.cur == self.goal:
            return False
        else:
            return True


with open("data1", "r") as file:
    inst_seq = file.readline().strip()
    data = file.read().strip()


sol = d8p1(data, "AAA", "ZZZ")

lost = True
while lost:
    lost = sol.step(inst_seq)


print(f"Step took: {sol.ct}")
