def input():
    with open('input.txt', 'r') as file:
        text = file.read()
        lines = text.split("\n")
    return lines

def parse(data):
    res = []
    for line in data:
        r = []
        for c in line:
            r.append(int(c))
        res.append(r)
    return res

def valid_coord(x,y, data):
    return not (x < 0 or y < 0 or y >= len(data) or x >= len(data[0]))

def visit_neighbours(queue, input, x, y):
    point = input[y][x]
    dir = (0,-1)
    for i in range(4):
        nx = x + dir[0]
        ny = y + dir[1]
        if valid_coord(nx,ny,input) and input[ny][nx] == point + 1:
            queue.append((nx,ny))
        if dir[0] == 0:
            dir = (dir[1]*-1, 0)
        else:
            dir = (0, dir[0]*1)
    return queue


def traverse(input, x, y):
    queue = [(x,y)]
    reached = []
    res = 0
    res2 = 0
    while queue:
        x, y = queue.pop(0)
        
        point = input[y][x]
        if point == 9:
            if (x,y) not in reached:
                reached.append((x,y))
                res += 1
            res2 += 1
        else:
            queue = visit_neighbours(queue, input, x, y)
    return res, res2

def solve(data):
    input = parse(data)
    res = 0
    res2 = 0
    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] == 0:
                r, r2 = traverse(input, x, y)
                res += r
                res2 += r2
    return res, res2

if __name__ == "__main__":
    data = input()
    p1, p2 = solve(data)
    print("part 1:", p1)
    print("part 2:", p2)