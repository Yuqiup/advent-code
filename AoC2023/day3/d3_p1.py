def check_neighbour(arr, x_loc, y_loc, x_len):
    patt = "0123456789."
    N_x = len(arr[0])
    N_y = len(arr)
    # row search
    for y_idx in (y_loc - 1, y_loc + 1):
        if y_idx < 0 or y_idx >= N_y:
            continue
        for i in range(x_len + 2):
            x_idx = x_loc + i - 1
            if x_idx < 0 or x_idx >= N_x:
                continue
            if arr[y_idx][x_idx] not in patt:
                return True

    if x_loc != 0:
        if arr[y_loc][x_loc - 1] not in patt:
            return True

    if x_loc != N_x - 1:
        if arr[y_loc][x_loc + x_len] not in patt:
            return True

    return False


with open("data1", "r") as file:
    sch = ["." + line.replace("\n", "") + "." for line in file]


N_x = len(sch[0])
N_y = len(sch)

result = 0
temp_num = ""
x_loc = 0
y_loc = 0
x_len = 0

for i_y in range(N_y):
    x_len = 0
    for i_x in range(N_x):
        if sch[i_y][i_x].isdigit():
            if x_len == 0:
                x_loc = i_x
                y_loc = i_y

            temp_num += sch[i_y][i_x]
            x_len += 1
        elif x_len > 0:
            print(temp_num)
            print(x_loc, y_loc, x_len)
            if check_neighbour(sch, x_loc, y_loc, x_len):
                print("hit" + temp_num)
                print(x_loc, y_loc, x_len)
                result += int(temp_num)
            temp_num = ""
            x_len = 0

print(result)
