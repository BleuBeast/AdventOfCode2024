import os

file_name = "../Input/day_6_input.txt"
dir_name = os.path.dirname(__file__)
file_path = os.path.join(dir_name, file_name)

guard_map = []

with open(file_path, "r") as file:
    lines = file.readlines()
    for line in lines:
        guard_map.append(line.strip())

def get_starting_position(path_map):
    for l_num, line in enumerate(path_map):
        for c_num, char in enumerate(line):
            if char == '^':
                return [l_num, c_num]
    return -1

def move(dir, cur_pos, g_map):
    g_map[cur_pos[0]] = g_map[cur_pos[0]][:cur_pos[1]] + 'X' + g_map[cur_pos[0]][cur_pos[1] + 1:]
    if dir == 'U':
        if 0 <= (cur_pos[0] - 1) < len(g_map) and g_map[cur_pos[0] - 1][cur_pos[1]] == '#':
            dir = 'R'
        else:
            cur_pos[0] -= 1
    elif dir == 'D':
        if 0 <= (cur_pos[0] + 1) < len(g_map) and g_map[cur_pos[0] + 1][cur_pos[1]] == '#':
            dir = 'L'
        else:
            cur_pos[0] += 1
    elif dir == 'L':
        if 0 <= (cur_pos[1] - 1) < len(g_map) and g_map[cur_pos[0]][cur_pos[1] - 1] == '#':
            dir = 'U'
        else:
            cur_pos[1] -= 1
    elif dir == 'R':
        if 0 <= (cur_pos[1] + 1) < len(g_map) and g_map[cur_pos[0]][cur_pos[1] + 1] == '#':
            dir = 'D'
        else:
            cur_pos[1] += 1
    return [dir, cur_pos, g_map]

current_pos = get_starting_position(guard_map)
direction = 'U'

if current_pos == -1:
    print("Invalid Map")
    quit

while current_pos[0] >= 0 and current_pos[0] < len(guard_map) and current_pos[1] >= 0 and current_pos[1] < len(guard_map[0]):
    move_result = move(direction, current_pos, guard_map)
    direction = move_result[0]
    current_pos = move_result[1]
    guard_map = move_result[2]

print(current_pos)
x_count = 0
for line in guard_map:
    for char in line:
        if char == 'X':
            x_count += 1
    print(line)

print(x_count)

