import os

file_name = "../Input/day_2_input.txt"
dir_name = os.path.dirname(__file__)
file_path = os.path.join(dir_name, file_name)

reports = []

with open(file_path, "r") as file:
    lines = file.readlines()
    reports = lines

def check_report(report_data):
    def is_decreasing(data):
        for i in range(len(data) - 1):
            difference = int(data[i]) - int(data[i + 1])
            if difference < 1 or difference > 3:
                return False
        return True
    
    def is_increasing(data):
        for i in range(len(data) - 1):
            difference = int(data[i]) - int(data[i + 1])
            if difference > -1 or difference < -3:
                return False
        return True
    
    if is_decreasing(report_data) or is_increasing(report_data):
        return True

    for i in range(len(report_data)):
        modified_report = report_data[:i] + report_data[i + 1:]
        if is_decreasing(modified_report) or is_increasing(modified_report):
            return True

    return False

valid_report_count = 0

while len(reports) > 0:
    report_data = reports.pop().strip().split(" ")
    if check_report(report_data):
        valid_report_count += 1

print(valid_report_count)