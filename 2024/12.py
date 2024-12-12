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

def change_dir(dir):
    if dir[0] == 0:
        dir = (dir[1]*-1, 0)
    else:
        dir = (0, dir[0]*1)
    return dir

def fence(x,y, input):
    plant = input[y][x]
    visited = [(x,y)]
    queue = [(x,y)]
    area = 1
    perimeter = 0
    sides = {}
    while queue:
        pos = queue.pop(0)
        dir = (0, -1)
        for i in range(4):
            x = pos[0] + dir[0]
            y = pos[1] + dir[1]
            if not valid_coord(x,y,input) or input[y][x] != plant:
                perimeter +=1
                if dir not in sides.keys():
                    sides[dir] = [(x,y)]
                else:
                    sides[dir].append((x,y))
            elif input[y][x] == plant and (x,y) not in visited:
                visited.append((x,y))
                area += 1
                queue.append((x,y))
            
            dir = change_dir(dir)
                
    side = 0
    for key in sides.keys():
        if key == (0, -1) or key == (0, 1):    
            s = sides[key]
            s.sort(key=lambda x: (x[1], x[0]))
            side += 1
            for i in range(len(s)-1):
                if s[i][1] != s[i+1][1]:
                    side +=1
                elif abs(s[i][0] - s[i+1][0]) > 1 and s[i][1] == s[i+1][1]:
                    side += 1
        else:
            s = sides[key]
            s.sort(key=lambda x: (x[0], x[1]))
            side += 1
            for i in range(len(s)-1):
                if s[i][0] != s[i+1][0]:
                    side +=1
                elif abs(s[i][1] - s[i+1][1]) > 1 and s[i][0] == s[i+1][0]:
                    side +=1

    return area*perimeter, area*side, visited

def solve(data):
    input = parse(data)
    visited = []
    res = 0 
    res2 = 0
    for y in range(len(input)):
        for x in range(len(input[y])):
            if (x,y) not in visited:
                visited.append((x,y))
                r, r2, v = fence(x,y,input)
                res += r
                res2 += r2
                visited += v
    return res, res2

if __name__ == "__main__":
    data = input()
    p1,p2 = solve(data)
    print("part 1:", p1)
    print("part 2:", p2)