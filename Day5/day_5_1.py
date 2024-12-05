import os

file_name = "../Input/day_5_input.txt"
dir_name = os.path.dirname(__file__)
file_path = os.path.join(dir_name, file_name)

rules = {}
updates = []
on_updates = False

with open(file_path, "r") as file:
    lines = file.readlines()
    for line in lines:
        if line == '\n':
            on_updates = True
        elif not on_updates:
            rule = line.strip().split('|')
            if int(rule[0]) in rules:
                rules[int(rule[0])].append(int(rule[1]))
            else:
                rules[int(rule[0])] = [int(rule[1])]
        elif on_updates:
            update = []
            for num in line.strip().split(','):
                update.append(int(num))
            updates.append(update)

def check_rules(update):
    # There has to be a better way to do this :'(
    for pos, page in enumerate(update):
        if page in rules:
            for num in rules[page]:
                for check in update[:pos]:
                    if num == check:
                        return False
    return True

def get_middle(update):
    # There is probably a better way to write this but it works
    middle = int(len(update) / 2)
    return update[middle]


sum_of_middles = 0

for update in updates:
    valid = check_rules(update)

    if valid:
        sum_of_middles += get_middle(update)

print(sum_of_middles)