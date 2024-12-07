from collections import defaultdict
def read_and_process_file(filename):
    updates = []
    must_be_after = defaultdict(set)
    section_flag = True
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line == "":
                section_flag = False
                continue
            if section_flag:
                key, value = line.split("|")
                must_be_after[key].add(value)
            else:
                updates.append(line.split(","))
    return must_be_after, updates


# print(must_be_after)

def is_in_right_order(must_be_after, update):
    for i in range(len(update) - 1):
        for j in range(i + 1, len(update)):
            if update[i] in must_be_after[update[j]]:
                return False
    return True


def correct_order(must_be_after, update):
    needs_adjustment = True
    while needs_adjustment:
        needs_adjustment = False
        i = 0
        while i < len(update) - 1:
            adjusted = False
            for j in range(i + 1, len(update)):
                if update[i] in must_be_after[update[j]]:
                    element = update.pop(i)
                    update.insert(j, element)
                    adjusted = True
                    needs_adjustment = True
                    break
            if not adjusted:
                i += 1  
        
    
    
def get_middle_num(update):
    if len(update) > 1:
        return int(update[len(update) // 2])
    return 0

sum_ = 0
# part 1
# for update in updates:
#     if is_in_right_order(must_be_after, update):
#         sum_ += get_middle_num(update)
        
# part 2
must_be_after, updates = read_and_process_file("input/day5.txt")

for update in updates:
    if not is_in_right_order(must_be_after, update):
        correct_order(must_be_after, update)
        sum_ += get_middle_num(update)

print(sum_)