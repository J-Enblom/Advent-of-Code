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

def mul(x,y):
    return x*y

def add(x,y):
    return x+y

def concat(x,y):
    return int(str(x)+str(y))

def part1(data):
    input = parse(data)
    tot = 0
    for line in input:
        res = int(line.split(":")[0])
        eq = [int(x) for x in line.split(":")[1][1:].split(" ")]
        paths = []
        for i in range(len(eq)-1):
            if i == 0:
                paths.append(mul(eq[i],eq[i+1]))
                paths.append(add(eq[i],eq[i+1]))
                paths.append(concat(eq[i],eq[i+1]))
            else:
                newm = []
                for x in paths:
                    newm.append(mul(x,eq[i+1]))
                    newm.append(add(x,eq[i+1]))
                    newm.append(concat(x,eq[i+1]))
                paths = newm
        
        for x in paths:
            if x == res:
                tot += res
                break

    return tot

def part2(data):
    return None

if __name__ == "__main__":
    data = input()
    print("part 1:", part1(data))
    print("part 2:", part2(data))