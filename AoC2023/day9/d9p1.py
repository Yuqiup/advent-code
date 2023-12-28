import numpy as np


class solver:
    def __init__(self, puzzle_input):
        self.arr = puzzle_input
        self.end = puzzle_input[-1]
        self.steps = 0

    def step(self):
        self.steps += 1
        while True:
            self.arr = np.diff(self.arr)
            self.end += self.arr[-1]
            if not any(self.arr):
                break


with open("data1", "r") as file:
    puzzle_input = file.read()

puzzle_input = puzzle_input.strip().split("\n")
puzzle_input = [i.split() for i in puzzle_input]

s = 0
for l in puzzle_input:
    sol = solver([int(n) for n in l])
    sol.step()
    s += sol.end

print(s)
