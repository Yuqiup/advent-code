import numpy as np
import sys

# spd = t_hold
# d = spd * (t_toltal - spd)
# 0 = - spd**2 + t_total * spd - d_goal

def solve_for_speed(t_total, d_goal):
    a = -1
    b = t_total
    c = -d_goal
    d = b**2 - 4*a*c
    if d < 0:                   # no solution
        return 0
    sol1 = (-b - np.sqrt(d)) / (2*a)
    sol2 = (-b + np.sqrt(d)) / (2*a)

    print (sol1, sol2)
    min_sol = min(sol1, sol2)
    max_sol = min(max(sol1, sol2), t_total +.1)
    if np.floor(min_sol) == min_sol:
        min_sol += 1
    if np.ceil(max_sol) == max_sol:
        max_sol -= 1

    print(f'min_sol: {min_sol}, max_sol: {max_sol}')
    return int(np.floor(max_sol) - np.ceil(min_sol) + 1)


with open('data2', 'r') as file:
    lines = file.readlines()

t_l = int(lines[0].split(':')[1].strip().replace(' ', ''))
d_l = int(lines[1].split(':')[1].strip().replace(' ', ''))


sol = solve_for_speed(t_l, d_l)
print(sol)
