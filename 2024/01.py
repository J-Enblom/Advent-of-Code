def input():
    with open('input.txt', 'r') as file:
        text = file.read()
        lines = text.split("\n")

    return lines

def part1(data):
    left = []
    right = []
    for line in data:
        line = line.split()
        left.append(int(line[0]))
        right.append(int((line[1])))
    left.sort()
    right.sort()
    res = 0
    for i in range(len(left)):
        res+= abs(left[i]-right[i])
    return res

def part2(data):
    left = []
    right = {}
    for line in data:
        line = line.split()
        left.append(int(line[0]))
        rightN = int(line[1])
        if rightN in right.keys():
            right[rightN] +=1
        else:
            right[rightN] = 1
    res = 0
    for i in range(len(left)):
        if left[i] in right.keys():
            res += left[i] * right[left[i]]
    return res

if __name__ == "__main__":
    data = input()
    print("part 1:", part1(data))
    print("part 2:", part2(data))