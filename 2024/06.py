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
    
    while walking:
        x = pos[0] + dir[0]
        y = pos[1] + dir[1]
        print("pos: ", pos, "dir: ", dir)
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

    return res

def part2(data):
    return None

if __name__ == "__main__":
    data = input()
    print("part 1:", part1(data))
    print("part 2:", part2(data))