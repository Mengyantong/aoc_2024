
def read_and_process_file(filename):
    list1 = []
    list2 = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 2:
                list1.append(int(parts[0]))
                list2.append(int(parts[1]))

    return list1, list2

def get_difference_sum(list1, list2):
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)
    total_difference_sum = sum(abs(x - y) for x, y in zip(sorted_list1, sorted_list2))
    print(total_difference_sum)

def get_appear_time(list1, list2):
    total_time = 0
    for i in list1:
        total_time += list2.count(i) * i
    print(total_time)
       
list1, list2 = read_and_process_file('input/day1.txt')

# part1
# get_difference_sum(list1, list2)

# part2
get_appear_time(list1, list2)