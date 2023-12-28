class loopy:
    def __init__(self, loop_map):
        self.coor = [0, 0]
        self.lmap = loop_map
        self.ylim = len(loop_map)
        self.xlim = len(loop_map[0])
        self.nxt_dir = [0, 0]
        self.step = 0
        self.visited = []

        self.con_dict = {
            "S": [[0, 1], [0, -1], [1, 0], [-1, 0]],
            "|": [[1, 0], [-1, 0]],
            "-": [[0, 1], [0, -1]],
            "F": [[1, 0], [0, 1]],
            "J": [[-1, 0], [0, -1]],
            "7": [[0, -1], [1, 0]],
            "L": [[-1, 0], [0, 1]],
            ".": [],
        }
        self.find_start()
        while True:
            print(f"step {self.step} at {self.coor}")
            check = self.find_next()
            if check:
                print(f"loop reached at {self.coor} in {self.step} steps")
                break

    def find_start(self):
        for i, l in enumerate(self.lmap):
            for j, c in enumerate(l):
                if c == "S":
                    self.coor = self.get_dir([i, j])
                    self.step += 1
                    self.visited = [[i, j]] + self.coor

    def find_next(self):
        c_ls = []
        for c in self.coor:
            # print(c)
            c_ls += self.get_dir(c)

        # print(c_ls)
        u_c_ls = []
        for c in c_ls:
            if c not in u_c_ls:
                u_c_ls.append(c)
        self.coor = u_c_ls
        self.step += 1

        return len(u_c_ls) == 1

    def bound_check(self, coor):
        return (
            coor[0] >= 0
            and coor[0] < self.ylim
            and coor[1] >= 0
            and coor[1] < self.xlim
        )

    def get_dir(self, coor):
        cur_sym = self.lmap[coor[0]][coor[1]]
        cor_diff = self.con_dict[cur_sym]
        # print("get dir", coor, cur_sym, cor_diff)
        coor_ls = []
        for cd in cor_diff:
            nxt_coor = [coor[0] + cd[0], coor[1] + cd[1]]
            nxt_sym = self.lmap[nxt_coor[0]][nxt_coor[1]]
            nxt_diff = self.con_dict[nxt_sym]
            # print("next_sym", nxt_coor, nxt_sym, nxt_diff)
            con_coor = [[nxt_coor[0] + c[0], nxt_coor[1] + c[1]] for c in nxt_diff]
            # print(con_coor)
            if (
                coor in con_coor
                and self.bound_check(nxt_coor)
                and nxt_coor not in self.visited
            ):
                self.visited.append(nxt_coor)
                coor_ls.append(nxt_coor)
        # print("qualified node", coor_ls)
        return coor_ls

    def is_point_in_loop(self, point):
        loop = self.visited
        x, y = point
        inside = False

        for i in range(len(loop)):
            j = (i + 1) % len(loop)
            xi, yi = loop[i]
            xj, yj = loop[j]
            if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi):
                inside = not inside
        return inside


with open("data1", "r") as file:
    node_map = file.read().splitlines()

sol = loopy(node_map)
