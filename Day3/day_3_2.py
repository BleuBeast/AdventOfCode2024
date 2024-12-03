import os

file_name = "../Input/day_3_input.txt"
dir_name = os.path.dirname(__file__)
file_path = os.path.join(dir_name, file_name)

corruption = []
with open(file_path, "r") as file:
    lines = file.readlines()
    test_data = ''
    for line in lines:
        cleaned_line = line.strip()
        test_data = test_data + cleaned_line
    do_its = test_data.split('do()')
    for split in do_its:
        corruption.append(split)

sum_of_multiplications = 0

for element in corruption:
    donts = element.split('don\'t()')
    for mult in donts[0].split('mul('):
        try:
            numbers = mult.split(')')
            numbers_split = numbers[0].split(',')
            if len(numbers_split) == 2:
                number_1 = int(numbers_split[0])
                number_2 = int(numbers_split[1])
                sum_of_multiplications += (number_1 * number_2)
        except:
            pass

print("Final Sum", sum_of_multiplications)