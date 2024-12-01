import os

file_name = "day_1_input.txt"
dir_name = os.path.dirname(__file__)
file_path = os.path.join(dir_name, file_name)

left_col = []
right_col = []

with open(file_path, "r") as file:
    lines = file.readlines()
    for line in lines:
        cleaned_line = line.strip().split('   ')
        left_col.append(int(cleaned_line[0]))
        right_col.append(int(cleaned_line[1]))

left_col.sort(reverse=True)
right_col.sort(reverse=True)

total_distance = 0

while len(left_col) > 0:
    total_distance += abs(left_col.pop() - right_col.pop())

print(total_distance)