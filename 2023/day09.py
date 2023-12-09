def input():
    with open('input.txt', 'r') as file:
        text = file.read()
        lines = text.split("\n")
    return lines

def parse(data):
    res = []
    for line in data:
        res.append([int(x) for x in line.split()])

    return res

def rec_finder(seq):
    i = 0
    differences = []
    while i < len(seq) - 1:
        differences.append(seq[i+1]- seq[i])
        i += 1
    if all(v == 0 for v in differences):
        return seq[-1]
    dif = rec_finder(differences)
    return seq[-1] + dif

def part1(data):
    input = parse(data)
    total = 0
    for seq in input:
        total += rec_finder(seq)
    return total

def rec_finder2(seq):
    i = 0
    differences = []
    while i < len(seq) - 1:
        differences.append(seq[i+1]- seq[i])
        i += 1
    if all(v == 0 for v in differences):
        return seq[0]
    dif = rec_finder2(differences)
    return seq[0] - dif

def part2(data):
    input = parse(data)
    total = 0
    for seq in input:
        total += rec_finder2(seq)
    return total

if __name__ == "__main__":
    data = input()
    print("part 1:", part1(data))
    print("part 2:", part2(data))