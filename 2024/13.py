import re
import numpy as np
def input():
    with open('input.txt', 'r') as file:
        text = file.read()
        lines = text.split("\n")
    return lines

def parse(data):
    res = []
    machine = []
    for line in data:
        if line != "":
            machine.append([int(x) for x in re.findall(r'\d+',line)])
        else:
            res.append(machine)
            machine = []
    return res

def part1(data):
    input = parse(data)
    res = 0
    for machine in input:
        ax = machine[0][0]
        ay = machine[0][1]
        bx = machine[1][0]
        by = machine[1][1]
        gx = machine[2][0]
        gy = machine[2][1]
        token = 0
        for b in range(100, -1, -1):
            for a in range(0, 101):
                if bx*b + ax*a == gx and by*b + ay*a == gy:
                    token += (b + 3*a)
                if token != 0:
                    break
            if token != 0:
                break
        res += token
    return res

def part2(data):
    input = parse(data)
    res = 0
    for machine in input:
        ax = machine[0][0]
        ay = machine[0][1]
        bx = machine[1][0]
        by = machine[1][1]
        i = 10000000000000
        gx = machine[2][0] + i
        gy = machine[2][1] + i
        a = np.array([[ax, bx], [ay, by]])
        b = np.array([gx,gy])
        x = np.linalg.solve(a,b)
        a = round(x[0])
        b = round(x[1])
        if a >= 0 and b >= 0:
            if bx*b + ax*a == gx and by*b + ay*a == gy:
                res += (3*a + b)
            

    return int(res)

if __name__ == "__main__":
    data = input()
    print("part 1:", part1(data))
    print("part 2:", part2(data))