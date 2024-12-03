import os

file_name = "../Input/day_3_input.txt"
dir_name = os.path.dirname(__file__)
file_path = os.path.join(dir_name, file_name)

corruption = []

with open(file_path, "r") as file:
    lines = file.readlines()
    for line in lines:
        cleaned_line = line.strip()
        for split in cleaned_line.split('mul('):
            corruption.append(split)

sum_of_multiplications = 0

for element in corruption:
    try:
        numbers = element.split(')')
        numbers_split = numbers[0].split(',')
        if len(numbers_split) == 2:
            number_1 = int(numbers_split[0])
            number_2 = int(numbers_split[1])
            print("Multiplying", number_1, number_2, "Error Check", numbers_split)
            sum_of_multiplications += (number_1 * number_2)
    except:
        pass

print("Final Sum", sum_of_multiplications)