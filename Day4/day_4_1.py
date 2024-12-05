import os

file_name = "../Input/day_4_input.txt"
dir_name = os.path.dirname(__file__)
file_path = os.path.join(dir_name, file_name)

word_search = []

with open(file_path, "r") as file:
    lines = file.readlines()
    for line in lines:
        word_search.append(line.strip())

def check_around(w_search, row, col):
    cases = [
        [(1, 0), (2, 0), (3, 0)],
        [(-1, 0), (-2, 0), (-3, 0)],
        [(0, 1), (0, 2), (0, 3)],
        [(0, -1), (0, -2), (0, -3)],
        [(1, 1), (2, 2), (3, 3)],
        [(-1, -1), (-2, -2), (-3, -3)],
        [(-1, 1), (-2, 2), (-3, 3)],
        [(1, -1), (2, -2), (3, -3)],
    ]
    valid_cases = 0
    for case in cases:
        try:
            if w_search[row - case[0][0]][col - case[0][1]] == 'M' and w_search[row - case[1][0]][col - case[1][1]] == 'A'and w_search[row - case[2][0]][col - case[2][1]] == 'S':
                if col - case[0][1] >= 0 and col - case[1][1] >= 0 and col - case[2][1] >= 0:
                    if row - case[0][0] >= 0 and row - case[1][0] >= 0 and row - case[2][0] >= 0:
                        valid_cases += 1
        except:
            pass
    return valid_cases

total_words = 0
for row, line in enumerate(word_search):
    for col, char in enumerate(line):
        if char == 'X':
            total_words += check_around(word_search, row, col)

print(total_words)