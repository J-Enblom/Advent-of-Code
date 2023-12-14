from math import ceil

def input():
    with open('input.txt', 'r') as file:
        text = file.read()
        lines = text.split("\n")
    return lines

def parse(data):
    res = []
    lines = []
    for line in data:
        if line == "":
            res.append(lines)
            lines = []
        else:
            lines.append(line)
    res.append(lines)
    return res


def find_vertical(pattern):
    length = len(pattern[0])
    index = 0
    for i in range(length - 1):
        errors = 0
        for x in range(length):
            left = i -x
            right = i + 1 + x
            if 0<=left<right<length:
                for row in range(len(pattern)):
                    if pattern[row][left] != pattern[row][right]:
                        errors += 1
        if errors == 1:
            index = i+1
    return index

            

def rec_horizontal(patternf, patternb):
    if not patternf or not patternb:
        return True
    if patternf[-1] == patternb[0]:
        return rec_horizontal(patternf[:-1], patternb[1:])
    return False


def find_horizontal(pattern):
    length = len(pattern)
    index = 0
    for i in range(length - 1):
        errors = 0
        for x in range(length):
            up = i -x
            down = i + 1 + x
            if 0<=up<down<length:
                for col in range(len(pattern[0])):
                    if pattern[up][col] != pattern[down][col]:
                        errors += 1
        if errors == 1:
            index = (i+1)*100
    return index

def part1(data):
    total = 0
    input = parse(data)
    for pattern in input:
        total += find_vertical(pattern)
        total += find_horizontal(pattern)
    return total

def part2(data):
    return None

if __name__ == "__main__":
    data = input()
    print("part 1:", part1(data))
    print("part 2:", part2(data))