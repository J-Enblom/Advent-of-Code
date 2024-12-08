
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

def valid_coord(x,y, data):

    return not (x < 0 or y < 0 or y >= len(data) or x >= len(data[0]))


def part1(data):
    input = parse(data)
    antenna = {}
    for y in range(len(input)):
        for x in range(len(input[y])):
            c = input[y][x]
            if c != ".":
                if c in antenna.keys():
                    antenna[c].append((x,y))
                else:
                    antenna[c] = [(x,y)]
    for key in antenna.keys():
        for i in range(len(antenna[key])):
            current = antenna[key][i]
            for s in range(len(antenna[key])):
                if s != i:
                    next = antenna[key][s]
                    x = current[0] + (current[0]-next[0])
                    y = current[1] + (current[1]-next[1])
                    if valid_coord(x,y,input):
                        input[y] = input[y][:x] + "#" + input[y][x+1:]

    res = 0
    for line in input:
        for c in line:
            if c == "#":
                res += 1
    return res

def part2(data):
    input = parse(data)
    antenna = {}
    for y in range(len(input)):
        for x in range(len(input[y])):
            c = input[y][x]
            if c != ".":
                if c in antenna.keys():
                    antenna[c].append((x,y))
                else:
                    antenna[c] = [(x,y)]
    for key in antenna.keys():
        for i in range(len(antenna[key])):
            current = antenna[key][i]
            for s in range(len(antenna[key])):
                if s != i:
                    next = antenna[key][s]
                    x = current[0] + (current[0]-next[0])
                    y = current[1] + (current[1]-next[1])
                    while valid_coord(x,y,input):
                        input[y] = input[y][:x] + "#" + input[y][x+1:]
                        x += (current[0]-next[0])
                        y += (current[1]-next[1])

    res = 0
    for line in input:
        for c in line:
            if c != ".":
                res += 1
    return res

if __name__ == "__main__":
    data = input()
    print("part 1:", part1(data))
    print("part 2:", part2(data))