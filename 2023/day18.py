def input():
    with open('input.txt', 'r') as file:
        text = file.read()
        lines = text.split("\n")
    return lines

def parse(data):
    res = []
    for line in data:
        res.append(line.split(" "))
    return res

directions = {
    "R": (0,1),
    "L": (0,-1),
    "D": (1,0),
    "U": (-1,0)
}

def part1(data):
    input = parse(data)
    x = 0
    y = 0
    dug = [(y,x)]
    for command in input:
        dir = directions[command[0]]
        for _ in range(int(command[1])):
            x += dir[1]
            y += dir[0]
            if (y,x) not in dug: 
                dug.append((y,x))
    dug.sort()
    total = 0
    skip = False
    i = 0
    y = 0
    for i in range(0, len(dug)):
        if y != dug[i][0]:
            r = 0
            y = dug[i][0]
            
        
        if skip:
            skip = False
            continue

        if len(dug)-1 == i:
            total +=1
            break
        
        if dug[i][0] == dug[i+1][0]:
            x = abs((dug[i+1][1]- dug[i][1]))
            if x > 1:
                if r % 2 == 0:
                    total += x
                    skip = True
                r+=1
        total += 1

    return total

def part2(data):
    return None

if __name__ == "__main__":
    data = input()
    print("part 1:", part1(data))
    print("part 2:", part2(data))