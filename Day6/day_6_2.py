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

possible_loop_count = 0

for l_num, line in enumerate(guard_map):
    if l_num % 10 == 0:
        print("On Line", l_num)
    for c_num, char in enumerate(line):
        temp_direction = direction
        temp_pos = current_pos[:]
        temp_guard_map = guard_map[:]
        temp_guard_map[l_num] = temp_guard_map[l_num][:c_num] + '#' + temp_guard_map[l_num][c_num + 1:]

        in_loop = []

        while temp_pos[0] >= 0 and temp_pos[0] < len(temp_guard_map) and temp_pos[1] >= 0 and temp_pos[1] < len(temp_guard_map[0]):
            if temp_guard_map[temp_pos[0]][temp_pos[1]] == 'X':
                if (temp_pos[0], temp_pos[1], temp_direction) in in_loop:
                    possible_loop_count += 1
                    break
                else:
                    in_loop.append((temp_pos[0], temp_pos[1], temp_direction))
            move_result = move(temp_direction, temp_pos, temp_guard_map)
            temp_direction = move_result[0]
            temp_pos = move_result[1]
            temp_guard_map = move_result[2]

print(possible_loop_count)

