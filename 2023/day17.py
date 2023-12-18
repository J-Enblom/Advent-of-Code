from math import inf

def input():
    with open('input.txt', 'r') as file:
        text = file.read()
        lines = text.split("\n")
    return lines

def parse(data):
    res = []
    y = 0
    for line in data:
        x = 0
        for cost in line:
            node = {"coord": (y,x), "dir": (), "cost": (inf, int(cost))}
            res.append(node)
            x +=1
        y +=1
    return res

def find_neighbours(current, unvisited):
    cx = current["coord"][1]
    cy = current["coord"][0]
    neighbours = []
    for node in unvisited:
        nx = node["coord"][1]
        ny = node["coord"][0]
        if abs(nx-cx) + abs(ny-cy) == 1:
            neighbours.append(node)

    return neighbours


def calc_dist(current, neighbours):
    cost = current["cost"][0] + current["cost"][1]
    for node in neighbours:
        dir = (node["coord"][0] - current["coord"][0], node["coord"][1] - current["coord"][1])
        if dir in current["dir"]:
            count = current["dir"][1]
            if count == 3:
                continue
            else:
                new_dir = (dir, count + 1)
        else:
            new_dir = (dir, 1)
        if cost < node["cost"][0]:
            node["dir"] = new_dir
            node["cost"] = (cost, node["cost"][1])
        

def find_next(unvisited):
    next = ""
    cost = inf
    for node in unvisited:
        if node["cost"][0] + node["cost"][1] < cost:
            cost = node["cost"][0] + node["cost"][1]
            next = node
    return next


def part1(data):
    unvisited = parse(data)
    visited = []
    start = unvisited[0]
    start["cost"] = (0, start["cost"][1])
    start["dir"] = ((0,1), 1)
    goal = unvisited[-1]
    goal_visited = False
    current = start
    while not goal_visited:
        neighbours = find_neighbours(current, unvisited)
        calc_dist(current, neighbours)
        visited.append(current)
        unvisited.remove(current)
        if goal in visited:
            goal_visited = True
        print(current)
        current = find_next(unvisited)

    return None

def part2(data):
    return None

if __name__ == "__main__":
    data = input()
    print("part 1:", part1(data))
    print("part 2:", part2(data))