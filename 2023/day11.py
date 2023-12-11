def input():
    with open('input.txt', 'r') as file:
        text = file.read()
        lines = text.split("\n")
    return lines

def parse(data):
    res = []
    for line in data:
        res.append(line.split()[0])
        if "#" not in line.split()[0]:
            res.append("x" * len(line.split()[0]))
    add_col = []
    for x in range(len(res[0])):
        add = True
        for y in range(len(res)):
            if res[y][x] == "#":
                add=False
                break
        if add:
            add_col.append(x)
    
    i = 0
    for coord in add_col:
        for y in range(len(res)):
            res[y] = res[y][:coord + i] + "x" + res[y][coord + i:]
        i +=1

    return res

def map_calc(stars):
    coords = {}
    i = 0
    y_adjust = 0
    for y in range(len(stars)):
        if stars[y].count("x") > 10:
            y_adjust += 999998
        else:
            x_adjust = 0
            for x in range(len(stars[y])):
                if stars[y][x] == "x":
                    x_adjust += 999998
                if stars[y][x] == "#":
                    coords[i] = (y + y_adjust, x + x_adjust)
                    i+=1
    print(coords)
    count = 0
    visisted = []
    for galaxy in coords.keys():
        for compare in coords.keys():
            if galaxy != compare and (galaxy, compare) not in visisted:
                x = abs(coords[galaxy][1] - coords[compare][1])
                y = abs(coords[galaxy][0] - coords[compare][0])
                visisted.append((compare, galaxy))
                count += x
                count += y

    return count

def part1(data):
    input = parse(data)
    total = map_calc(input)
    return total

def part2(data):
    input = parse(data)
    total = map_calc(input)
    return total

if __name__ == "__main__":
    data = input()
    #print("part 1:", part1(data))
    print("part 2:", part2(data))