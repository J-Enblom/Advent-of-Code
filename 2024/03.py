import re

def input():
    with open('input.txt', 'r') as file:
        text = file.read()
        lines = text.split("\n")
    return lines

def parse(data):
    res = []
    for line in data:
        res.append(line)
    return res

def part1(data):
    input = parse(data)
    nums = []
    for line in input:
        nums += (re.findall('mul\((\d+,\d+)\)',line))
    res = 0
    for x in nums:
        num = x.split(",")
        res += int(num[0])*int(num[1])
    return res

def part2(data):
    input = parse(data)
    res = 0
    test = ""
    correct = []
    for line in input:
        test += line
    
    donts = test.split("don't()")
    for i in range(len(donts)):
        if i == 0:
            correct.append(donts[i])
        else:
            dos = donts[i].split("do()")
            for y in range(len(dos)):
                if y == 0:
                    continue
                else:
                    correct.append(dos[y])
    
                        
    nums = []
    for line in correct:
        nums += (re.findall('mul\((\d+,\d+)\)',line))
    res = 0
    for x in nums:
        num = x.split(",")
        res += int(num[0])*int(num[1])
                    
    return res

if __name__ == "__main__":
    data = input()
    print("part 1:", part1(data))
    print("part 2:", part2(data))