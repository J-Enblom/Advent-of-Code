from functools import cache

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

def rec_solve(data):
    for i in range(1, len(data)):
        for x in range(len(data[i])):
            if data[i][x] == "O":
                for y in reversed(range(i)):
                    if data[y][x] == ".":
                        data[y] = data[y][:x] + "O" + data[y][x+1:]
                        data[y+1] = data[y+1][:x] + "." + data[y+1][x+1:]
                    else:
                        break
    return data
        

def part1(data):
    input = parse(data)
    for i in range(2, len(input)+1):
        input[:i] = rec_solve(input[:i])
    total = 0
    i = 0
    for line in reversed(range(len(input))):
        total += input[i].count("O") * (line+1)
        i += 1
    return total


@cache
def cycle(keys, values, mx, my):
    data = {}
    i = 0
    for key in keys:
        data[key] = values[i]
        i +=1
    for y in range(my):
        for x in range(mx):
            if data[(y,x)] == "O":
                i = y
                while i >= 0:
                    if (i - 1, x) in data.keys():
                        if data[(i - 1, x)] != ".":
                            data[(y,x)] = "."
                            data[(i,x)] = "O"
                            break
                    else:
                        data[(y,x)] = "."
                        data[(i,x)] = "O"
                        break
                    i -=1
    for y in range(my):
        for x in range(mx):
            if data[(y,x)] == "O":
                i = x
                while i >= 0:
                    if (y, i - 1) in data.keys():
                        if data[(y, i - 1)] != ".":
                            data[(y,x)] = "."
                            data[(y,i)] = "O"
                            break
                    else:
                        data[(y,x)] = "."
                        data[(y,i)] = "O"
                        break
                    i -=1
    for y in reversed(range(my)):
        for x in range(mx):
            if data[(y,x)] == "O":
                i = y
                while i >= 0:
                    if (i + 1, x) in data.keys():
                        if data[(i + 1, x)] != ".":
                            data[(y,x)] = "."
                            data[(i,x)] = "O"
                            break
                    else:
                        data[(y,x)] = "."
                        data[(i,x)] = "O"
                        break
                    i +=1
    for y in range(my):
        for x in reversed(range(mx)):
            if data[(y,x)] == "O":
                i = x
                while i >= 0:
                    if (y, i + 1) in data.keys():
                        if data[(y, i + 1)] != ".":
                            data[(y,x)] = "."
                            data[(y,i)] = "O"
                            break
                    else:
                        data[(y,x)] = "."
                        data[(y,i)] = "O"
                        break
                    i +=1
    return data

def part2(data):
    maxY = len(data)
    maxX = len(data[0])
    input = {}
    for y in range(len(data)):
        for x in range(len(data[y])):
            input[(y,x)] = data[y][x]
    history = []
    r = 1000000000
    while True:
        input = cycle(tuple(input.keys()), tuple(input.values()), maxY, maxX)
        if input in history:
            loop_start = history.index(input)
            loop_end = len(history)
            index = ((r - loop_start) % (loop_end - loop_start)) + loop_start -1
            output = history[index]
            break
        else:
            history.append(input)
    total = 0
    for key in output.keys():
        if output[key] == "O":
            total += maxY - key[0]
    return total

if __name__ == "__main__":
    data = input()
    print("part 1:", part1(data))
    print("part 2:", part2(data))