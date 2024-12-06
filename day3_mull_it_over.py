import re
def read_and_process_file(filename):
    content = ""
    with open(filename, 'r', encoding='utf-8') as file:
        # content = file.read()
        for line in file:
            content += line.strip()
        
    return content

def mul_patten_match(content):
    # mul(440,532)
    patten = r"mul\((\d+),(\d+)\)"
    matches = re.findall(patten, content)
    return sum(int(a) * int(b) for a, b in matches)
        
def content_after_dont(content):
    sum_ = 0
    patten = r"don't\(\)((?:(?!do\(\)|don't\(\)).)*)"
    matches = re.findall(patten, content)
    for match in matches:
        # print(match)
        sum_ += mul_patten_match(match)
    return sum_
    
content = read_and_process_file("input/day3.txt")
# part 1
print(mul_patten_match(content))

# part 2
print(mul_patten_match(content) - content_after_dont(content))