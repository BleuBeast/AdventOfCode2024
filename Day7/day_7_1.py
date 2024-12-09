import os

file_name = "../Input/day_7_input.txt"
dir_name = os.path.dirname(__file__)
file_path = os.path.join(dir_name, file_name)

values = {}

with open(file_path, "r") as file:
    lines = file.readlines()
    for line in lines:
        cleaned_line = line.strip()
        data = cleaned_line.split(": ")
        value = int(data[0])
        values[value] = []
        numbers = data[1].split(" ")
        for number in numbers:
            values[value].append(int(number))

sum_of_values = 0
largest_nums = 0

for value in values:
    quantity = len(values[value])
    combinations = pow(2, quantity) - 1

    current_num = 0
    while combinations > 0:
        binary_num = bin(combinations)[2:]
        binary_num = binary_num.zfill(quantity)

        for num_pos, num in enumerate(values[value]):
            if num_pos == 0:
                current_num = num
            else:
                if binary_num[num_pos] == "0":
                    current_num = current_num * num
                else:
                    current_num = current_num + num
        
        if current_num == value:
            sum_of_values = sum_of_values + current_num
            break
        else:
            combinations -= 1
            current_num = 0

print(sum_of_values)

# 3693757858 - Too Low
# 5540634308362