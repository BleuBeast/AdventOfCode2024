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

def to_ternary(num):
    if num == 0:
        return '0'
    digits = []
    while num:
        digits.append(str(num % 3))
        num //= 3
    return ''.join(reversed(digits))

sum_of_values = 0
largest_nums = 0

for v_num, value in enumerate(values):
    quantity = len(values[value])
    combinations = pow(3, quantity) - 1
    
    if v_num % 50 == 0:
        print("Completed", v_num)

    current_num = 0
    while combinations > 0:
        ternary_num = to_ternary(combinations)
        ternary_num = ternary_num.zfill(quantity)
        for num_pos, num in enumerate(values[value]):
            if num_pos == 0:
                current_num = num
            else:
                if ternary_num[num_pos] == "0":
                    current_num = current_num * num
                elif ternary_num[num_pos] == "1":
                    current_num = current_num + num
                else:
                    temp_num = str(current_num) + "" + str(num)
                    current_num = int(temp_num)
        
        if current_num == value:
            sum_of_values = sum_of_values + current_num
            break
        else:
            combinations -= 1
            current_num = 0

print(sum_of_values)