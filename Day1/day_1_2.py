import os

file_name = "day_1_input.txt"
dir_name = os.path.dirname(__file__)
file_path = os.path.join(dir_name, file_name)

left_col = []
right_col = {}

with open(file_path, "r") as file:
    lines = file.readlines()
    for line in lines:
        cleaned_line = line.strip().split('   ')
        left_col.append(int(cleaned_line[0]))
        right_num = int(cleaned_line[1])
        if right_num in right_col:
            right_col[right_num] += 1
        else:
            right_col[right_num] = 1

similarity_score = 0

while len(left_col) > 0:
    left_num = left_col.pop()
    if left_num in right_col:
        similarity_score += left_num * right_col[left_num]
    
print(similarity_score)