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

word = ["X", "M", "A", "S"]

def count(input, x, y, wIndex):
    res = 0
    taken = []
    for yd in range(0,2):
        for xd in range(0,2):
            if x >= xd and y >= yd:
                if input[y-yd][x-xd] == word[wIndex]:
                    if not (0-xd,0-yd) in taken:
                        res += countHelper(input, x-xd, 0-xd, y-yd, 0-yd, wIndex+1)
                        taken.append((0-xd,0-yd))
            if x <= len(input[y])-xd-1 and y <= len(input)-yd-1:
                if input[y+yd][x+xd] == word[wIndex]:
                    if not (xd,yd) in taken:
                        res += countHelper(input, x+xd, xd, y+yd, yd, wIndex+1)
                        taken.append((xd,yd))
            if x <= len(input[y])-xd-1 and y >= yd:
                if input[y-yd][x+xd] == word[wIndex]:
                    if not (xd,0-yd) in taken:
                        res += countHelper(input, x+xd, xd, y-yd, 0-yd, wIndex+1)
                        taken.append((xd,0-yd))
            if x >= xd and y <= len(input)-yd-1:
                if input[y+yd][x-xd] == word[wIndex]:
                    if not (0-xd,yd) in taken:
                        res += countHelper(input, x-xd, 0-xd, y+yd, yd, wIndex+1)
                        taken.append((0-xd,yd))
    return res

def countHelper(input, x, xd, y, yd, wIndex):
    if wIndex == 4:
        return 1
    res = 0
    if y+yd>= 0 and y+yd < len(input) and x+xd >= 0 and x+xd < len(input[y]): 
        if input[y+yd][x+xd] == word[wIndex]:
            res = countHelper(input, x+xd, xd, y+yd, yd, wIndex+1)
    return res

def part1(data):
    input = parse(data)
    res = 0
    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] == "X":
                res += count(input, x, y, 1)

    return res

def part2(data):
    input = parse(data)
    res = 0
    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] == "M":
                if x-2 >= 0:
                    if input[y][x-2] == "M":
                        if y+2 < len(input) and input[y+1][x-1] == "A" and input[y+2][x-2] == "S" and input[y+2][x] == "S":
                            res += 1
                            input[y] = input[y][:x] + "." + input[y][x+1:]
                        if y-2 >= 0 and input[y-1][x-1] == "A" and input[y-2][x-2] == "S" and input[y-2][x] == "S":
                            res += 1
                            input[y] = input[y][:x] + "." + input[y][x+1:]
                if x+2 < len(input[y]):
                    if input[y][x+2] == "M":
                        if y+2 < len(input) and input[y+1][x+1] == "A" and input[y+2][x+2] == "S" and input[y+2][x] == "S":
                            res += 1
                            input[y] = input[y][:x] + "." + input[y][x+1:]
                        if y-2 >= 0:
                            if input[y-1][x+1] == "A":
                                if input[y-2][x+2] == "S":
                                    if input[y-2][x] == "S":
                                        res += 1
                                        input[y] = input[y][:x] + "." + input[y][x+1:]
                if y-2 >= 0:
                    if input[y-2][x] == "M":
                        if x+2 < len(input[y]) and input[y-1][x+1] == "A" and input[y-2][x+2] == "S" and input[y][x+2] == "S":
                            res += 1
                            input[y] = input[y][:x] + "." + input[y][x+1:]
                        if x-2 >= 0 and input[y-1][x-1] == "A" and input[y-2][x-2] == "S" and input[y][x-2] == "S":
                            res += 1
                            input[y] = input[y][:x] + "." + input[y][x+1:]
                        
                if y+2 < len(input):
                    if input[y+2][x] == "M":
                        if x+2 < len(input[y]) and input[y+1][x+1] == "A" and input[y+2][x+2] == "S" and input[y][x+2] == "S":
                            res += 1
                            input[y] = input[y][:x] + "." + input[y][x+1:]
                        if x-2 >= 0:
                            if input[y+1][x-1] == "A":
                                if input[y+2][x-2] == "S":
                                    if input[y][x-2] == "S":
                                        res += 1
                                        input[y] = input[y][:x] + "." + input[y][x+1:]
    for y in input:
        print(y)
    return res

if __name__ == "__main__":
    data = input()
    print("part 1:", part1(data))
    print("part 2:", part2(data))