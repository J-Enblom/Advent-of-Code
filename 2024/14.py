from time import sleep
import numpy as np
from PIL import Image

def input():
    with open('input.txt', 'r') as file:
        text = file.read()
        lines = text.split("\n")
    return lines

def parse(data):
    res = []
    for line in data:
        robot = []
        temp = line.split(" ")
        v = temp[0]
        v = v[2:].split(",")
        robot.append((int(v[0]),int(v[1])))
        v = temp[1]
        v = v[2:].split(",")
        if "-" in v[0]:
            l = int(v[0][1:])*-1
        else:
            l = int(v[0])
        if "-" in v[1]:
            r = int(v[1][1:])*-1
        else:
            r = int(v[1])
        robot.append((l,r))
        res.append(robot)
        
        #print(temp)
        #res.append(line)
    return res

def solve(data, sec, width, length):
    tree = []
    for i in range(length):
        tree.append([[0,0,0]] * width)
    quad = {}
    quad["q1"] = []
    quad["q2"] = []
    quad["q3"] = []
    quad["q4"] = []
    robots = parse(data)
    for robot in robots:
        vx = robot[1][0]
        vy = robot[1][1]

        x = (robot[0][0] + vx * sec) % width
        y = (robot[0][1] + vy * sec) % length
        dx = width//2
        dy = length//2
        if x < dx and y < dy:
            quad["q1"].append((x,y))
        elif x > dx and y < dy:
            quad["q2"].append((x,y))
        elif x > dx and y > dy:
            quad["q4"].append((x,y))
        elif x < dx and y > dy:
            quad["q3"].append((x,y))
        tree[y][x] = [255,255,255]
    res = 1
    for q in quad.keys():
        res *= len(quad[q])
    ar = np.array(tree, dtype=np.uint8)
    image = Image.fromarray(ar)
    s = str(sec) + ".png"
    image.save(s)
    return res

def part2():
    i = 1
    while i < 9001:
        solve(data, i, 101, 103)
        print(i)
        i += 1

if __name__ == "__main__":
    data = input()
    #print("part 1:", solve(data, 100, 101, 103))
    print("part 2:", part2())