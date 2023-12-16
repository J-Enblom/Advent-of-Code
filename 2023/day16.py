from collections import Counter
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

def travel(data, curr, dir, visited):
    to_visit = []
    
    while True:
        if curr[0] < 0 or curr[0] >= len(data) or curr[1] < 0 or curr[1] >= len(data[0]):
            #print("break", curr)
            break
        if (curr,dir) in visited:
            break
        visited.append((curr,dir)) 
        #print(curr)
        if data[curr[0]][curr[1]] == "/":
            if dir == (0,1):
                dir = (-1,0)
            elif dir == (0,-1):
                dir = (1,0)
            elif dir == (1,0):
                dir = (0,-1)
            else:
                dir = (0,1)
        elif data[curr[0]][curr[1]] == "\\":
            if dir == (0,1):
                dir = (1,0)
            elif dir == (0,-1):
                dir = (-1,0)
            elif dir == (1,0):
                dir = (0,1)
            else:
                dir = (0,-1)
        elif data[curr[0]][curr[1]] == "-":
            if dir == (1,0) or dir == (-1,0):
                dir = (0,1)
                temp = (curr[0] + dir[0], curr[1] + dir[1])
                if (temp, dir) not in visited and (temp,dir) not in to_visit:
                        to_visit.append((temp, dir))
                dir = (0,-1)
        elif data[curr[0]][curr[1]] == "|":
            if dir == (0,1) or dir == (0,-1):
                dir = (1,0)
                temp = (curr[0] + dir[0], curr[1] + dir[1])
                if (temp, dir) not in visited and (temp, dir) not in to_visit:
                        to_visit.append((temp, dir))
                dir = (-1,0)

        curr = (curr[0] + dir[0], curr[1] + dir[1])

    for split_p in to_visit:
        if split_p not in visited:
            visited = travel(data, split_p[0], split_p[1], visited)
    return visited

def part1(data):
    input = parse(data)
    visited = []
    visited = travel(input, (0,0), (0,1), visited)
    visited = [x[0] for x in visited]
    res = len(Counter(visited).keys())

    return res

def part2(data):
    input = parse(data)
    tot = 0
    for y in range(len(input)):
        for x in range(len(input[y])):
            if x == 0 or x == len(input[y])-1 or y == 0 or y == len(input)-1:
                visited = []
                if x == 0:
                    vis = travel(input, (y,x), (0,1), visited)
                    vis = [x[0] for x in vis]
                    res = len(Counter(vis).keys())
                    if res > tot:
                        tot = res
                if x == len(input[y])-1:
                    vis = travel(input, (y,x), (0,-1), visited)
                    vis = [x[0] for x in vis]
                    res = len(Counter(vis).keys())
                    if res > tot:
                        tot = res
                if y == 0:
                    vis = travel(input, (y,x), (1,0), visited)
                    vis = [x[0] for x in vis]
                    res = len(Counter(vis).keys())
                    if res > tot:
                        tot = res
                if y == len(input)-1:
                    vis = travel(input, (y,x), (-1,0), visited)
                    vis = [x[0] for x in vis]
                    res = len(Counter(vis).keys())
                    if res > tot:
                        tot = res
    
    return tot



if __name__ == "__main__":
    data = input()
    print("part 1:", part1(data))
    print("part 2:", part2(data))