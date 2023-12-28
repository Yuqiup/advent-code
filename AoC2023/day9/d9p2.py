import numpy as np


class solver:
    def __init__(self, puzzle_input):
        self.arr = puzzle_input
        self.end = puzzle_input[-1]
        self.start = puzzle_input[0]
        self.steps = 0

    def step(self):
        while True:
            self.steps += 1
            self.arr = np.diff(self.arr)

            self.end += self.arr[-1]
            if self.steps % 2 != 0:
                self.start -= self.arr[0]

            else:
                self.start += self.arr[0]

            if not any(self.arr):
                break


with open("data2", "r") as file:
    puzzle_input = file.read()

puzzle_input = puzzle_input.strip().split("\n")
puzzle_input = [i.split() for i in puzzle_input]

s = 0
for l in puzzle_input:
    sol = solver([int(n) for n in l])
    sol.step()
    s += sol.start

print(s)
