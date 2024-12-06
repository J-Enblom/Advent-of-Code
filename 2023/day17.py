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
            node = {"coord": (y,x), "dir": ((0,0), 0), "cost": (inf, int(cost))}
            res.append(node)
            x +=1
        y +=1
    return res

def find_neighbours(current, unvisited):
    cx = current["coord"][1]
    cy = current["coord"][0]
    cdx = current["dir"][0][1]
    cdy = current["dir"][0][0]
    neighbours = []
    for node in unvisited:
        nx = node["coord"][1]
        ny = node["coord"][0]
        ndx = node["dir"][0][1]
        ndy = node["dir"][0][0]
        if abs(nx-cx) + abs(ny-cy) == 1 and not (cdx + ndx == 0 and cdy + ndy == 0):
            neighbours.append(node)

    return neighbours


def calc_dist(current, neighbours, open_set):
    cost = current["cost"][0] + current["cost"][1]
    for node in neighbours:
        dir = (node["coord"][0] - current["coord"][0], node["coord"][1] - current["coord"][1])
        if dir in current["dir"]:
            count = current["dir"][1]
            if count == 3:
                continue
            else:
                new_dir = (dir, count + 1)
                if cost < node["cost"][0]:
                    node["dir"] = new_dir
                    node["cost"] = (cost, node["cost"][1])
                    if node not in open_set:
                        open_set.append(node)
        else:
            new_node = {}
            new_node["coord"] = node["coord"]
            new_node["dir"] = (dir, 1)
            new_node["cost"] = (cost, node["cost"][1])
            if new_node not in open_set:
                open_set.append(new_node)
            
        

def find_next(unvisited):
    next = ""
    cost = inf
    for node in unvisited:
        if node["cost"][0] + node["cost"][1] < cost:
            cost = node["cost"][0] + node["cost"][1]
            next = node
    return next

def add_nodes(open_set, nodes):
    for node in open_set:
        if node not in open_set:
            nodes.append(node)

def debug_path(visited):
    current = visited[-1]
    path = []
    while True:
        path.insert(0, current)
        if current["coord"]== (0,0):
            break
        cy = current["coord"][0] - current["dir"][0][0]
        cx = current["coord"][1] - current["dir"][0][1]
        for node in visited:
            if node["coord"] == (cy, cx) and node["cost"][0] == current["cost"][0] - node["cost"][1]:
                current = node
                break

    for node in path:
        print(node)

def part1(data):
    nodes = parse(data)
    path = []
    open_set = []
    start = nodes[0]
    start["cost"] = (0, 0)
    start["dir"] = ((0,1), 1)
    goal = nodes[-1]
    open_set.append(start)
    current = start
    while open_set:
        if current["coord"] == goal["coord"]:
            path.append(current)
            break
        neighbours = find_neighbours(current, nodes)
        calc_dist(current, neighbours, open_set)
        open_set.remove(current)
        path.append(current)
        current = find_next(open_set)

    debug_path(path)

    return current["cost"][0] + current["cost"][1]

def part2(data):
    return None

if __name__ == "__main__":
    data = input()
    print("part 1:", part1(data))
    print("part 2:", part2(data))