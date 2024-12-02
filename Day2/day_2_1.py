import os

file_name = "../Input/day_2_input.txt"
dir_name = os.path.dirname(__file__)
file_path = os.path.join(dir_name, file_name)

reports = []

with open(file_path, "r") as file:
    lines = file.readlines()
    reports = lines

valid_report_count = 0

while len(reports) > 0:
    report_data = reports.pop().strip().split(" ")
    prev_value = int(report_data.pop())
    is_valid = True
    is_decreasing = None
    while len(report_data) > 0:
        current_value = int(report_data.pop())
        difference = prev_value - current_value
        if abs(difference) < 1 or abs(difference) > 3:
            is_valid = False
            break

        if is_decreasing is None:
            if difference > 0:
                is_decreasing = False
            elif difference < 0:
                is_decreasing = True
            else:
                print("This shouldn't be possible")
                break
        
        if is_decreasing and difference >= 0:
            is_valid = False
            break
        if not is_decreasing and difference <= 0:
            is_valid = False
            break

        prev_value = current_value
    
    if is_valid:
        valid_report_count += 1

print(valid_report_count)

# 3926 is Too High - I am actually so stupid, I don't wanna talk about it :'(
# I just didn't have the valid report count increment in the right spot

