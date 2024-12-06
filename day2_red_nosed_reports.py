def read_and_process_file(filename):
    reports = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split()
            parts_int = [int(part) for part in parts]
            reports.append(parts_int)
    return reports

def is_safe(levels):
    if len(levels) < 2:
        return False 

    increasing = True
    decreasing = True
    safe = True

    for i in range(1, len(levels)):
        diff = levels[i] - levels[i-1]
        if diff <= 0:
            increasing = False
        if diff >= 0:
            decreasing = False
        if abs(diff) > 3 or diff == 0:
            safe = False
            
    return (increasing or decreasing) and safe


# part 1
# count = 0
# for levels in read_and_process_file('input/day2.txt'):
#     if is_safe(levels):
#         count += 1
# print(count)

# part 2
count = 0
for levels in read_and_process_file('input/day2.txt'):
    if_safe = False
    for i in range(len(levels)):
        new_levels = levels[:]
        new_levels.pop(i)
        if is_safe(new_levels):
           if_safe = True
    if if_safe:
        count += 1
print(count)