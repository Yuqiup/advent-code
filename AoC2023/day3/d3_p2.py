def check_neighbour(arr, x_loc, y_loc):
    patt = "0123456789"
    N_x = len(arr[0])
    N_y = len(arr)

    pairs = []
    # first row
    y = y_loc - 1
    temp = -1
    for x in [x_loc - 1, x_loc, x_loc + 1]:
        if arr[y][x].isdigit():
            if temp != x:
                pairs.append((x, y))
            temp = x + 1

    y = y_loc + 1
    temp = -1
    for x in [x_loc - 1, x_loc, x_loc + 1]:
        if arr[y][x].isdigit():
            if temp != x:
                pairs.append((x, y))
            temp = x + 1

    y = y_loc
    x = x_loc - 1
    if arr[y][x].isdigit():
        pairs.append((x, y))

    x = x_loc + 1
    if arr[y][x].isdigit():
        pairs.append((x, y))

    return pairs


def backward_search(arr, num_str, x, y):
    s = num_str
    for i in range(x - 1):
        if arr[y][x - i - 1].isdigit():
            s = arr[y][x - i - 1] + s
        else:
            return s

    return s


def forward_search(arr, num_str, x, y):
    s = num_str
    for i in range(len(arr[0])):
        if arr[y][x + i + 1].isdigit():
            s = s + arr[y][x + i + 1]
        else:
            return s
    return s


with open("data2", "r") as file:
    sch = ["." + line.replace("\n", "") + "." for line in file]


N_x = len(sch[0])
N_y = len(sch)

sch = ["." * N_x] + sch + ["." * N_x]

result = 0
temp_num = ""

for y in range(N_y):
    for x in range(N_x):
        if sch[y][x] == "*":
            pairs = check_neighbour(sch, x, y)
            print(pairs)
            if len(pairs) == 2:
                s0 = sch[pairs[0][1]][pairs[0][0]]
                s1 = sch[pairs[1][1]][pairs[1][0]]
                s0 = backward_search(sch, s0, pairs[0][0], pairs[0][1])
                s0 = forward_search(sch, s0, pairs[0][0], pairs[0][1])
                s1 = backward_search(sch, s1, pairs[1][0], pairs[1][1])
                s1 = forward_search(sch, s1, pairs[1][0], pairs[1][1])
                print(s0, s1)
                result += int(s0) * int(s1)


print(result)
