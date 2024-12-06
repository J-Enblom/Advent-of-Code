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
    pos = (0,0)
    dir = (0,-1)
    res = 0
    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] == "^":
                pos = (x,y)
                input[y] = input[y][:x] + "X" + input[y][x+1:]
                res +=1
    walking = True
    start = (pos[0], pos[1])
    while walking:
        x = pos[0] + dir[0]
        y = pos[1] + dir[1]
        if x < 0 or y < 0 or y >= len(input) or x >= len(input[y]):
            walking = False
        else:
            if input[y][x] == "#":
                if dir[0] == 0:
                    dir = (dir[1]*-1, 0)
                else:
                    dir = (0, dir[0]*1)
            else:
                pos = (x, y)
                if input[y][x] == ".":
                    res +=1
                    input[y] = input[y][:x] + "X" + input[y][x+1:]
    for line in input:
        print(line)
    res2 = part2(input, start)
    return res, res2

def part2(data, start):
    original = data.copy()
    res = 0
    for yr in range(len(data)):
        for xr in range(len(data[yr])):
            dir = (0,-1)
            pos = (start[0], start[1])
            data = original.copy()
            visited = {}
            if data[yr][xr] != "#":
                data[yr] = data[yr][:xr] + "#" + data[yr][xr+1:]
                walking = True
            else:
                walking = False
            while walking:
                x = pos[0] + dir[0]
                y = pos[1] + dir[1]
                if x < 0 or y < 0 or y >= len(data) or x >= len(data[y]):
                    walking = False
                else:
                    if data[y][x] == "#":
                        if dir[0] == 0:
                            dir = (dir[1]*-1, 0)
                        else:
                            dir = (0, dir[0]*1)
                    else:
                        if pos in visited.keys():
                            if dir in visited[pos]:
                                res += 1
                                walking = False
                            else:
                                visited[pos].append(dir)
                        else:
                            visited[pos] = [dir]
                        pos = (x, y)
            print(visited, data)
                        

    return res





if __name__ == "__main__":
    data = input()
    p1, p2 = part1(data)
    print("part 1:", p1)
    print("part 2:", p2)