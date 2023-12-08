from math import gcd

def input():
    with open('input.txt', 'r') as file:
        text = file.read()
        lines = text.split("\n")
    return lines

def parse(data):
    res = data[0]
    path = {}
    for line in data[2:]:
        dest = line.split("=")[0].strip()
        paths = line.split("=")[1].strip().split(",") #Make tuple directly somehow?
        path[dest] = (paths[0][1:], paths[1][1:-1])
    return res, path

def part1(data):
    input, path = parse(data)
    current = "AAA"
    goal = "ZZZ"
    taken = 0

    while current != goal:
        for direction in input:
            if direction == "L":
                current = path[current][0]
                taken += 1
            else:
                current = path[current][1]
                taken += 1
            if current == goal:
                    break
    return taken

def part2(data):
    input, paths = parse(data)
    current = []
    for key in paths.keys():
        if key[-1] == "A":
            current.append(key)

    goal = []
    for path in current:
        step = 0
        while path[-1] != "Z":
            for direction in input:
                if direction == "L":
                    path = paths[path][0]
                    step += 1
                else:
                    path = paths[path][1]
                    step += 1
                if path[-1] == "Z":
                        break
        goal.append(step)
    
    lcm = 1
    for i in goal:
        lcm = lcm*i//gcd(lcm,i)

    return lcm

if __name__ == "__main__":
    data = input()
    print("part 1:", part1(data))
    print("part 2:", part2(data))