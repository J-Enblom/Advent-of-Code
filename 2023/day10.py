def input():
    with open('input.txt', 'r') as file:
        text = file.read()
        lines = text.split("\n")
    return lines

def parse(data):
    res = {}
    y = 0
    for line in data:
        x = 0
        for char in line:
            res[(x,y)] = char
            if char == "S":
                start = (x,y)
            x+=1
            
        y += 1
    return res, start

def traverse(paths, start):

    left = ["-", "L", "F"]
    right = ["-", "7", "J"]
    up = ["|", "7", "F"]
    down = ["|", "L", "J"]

    possible_paths = []
    current = start
    if (paths[(current[0], current[1] + 1)] in down):
        possible_paths.append((current[0], current[1] + 1))
    if (paths[(current[0], current[1] - 1)] in up):
        possible_paths.append((current[0], current[1] - 1))
    if (paths[(current[0] - 1, current[1])] in left):
        possible_paths.append((current[0] - 1, current[1]))
    if (paths[(current[0] + 1, current[1])] in right):
        possible_paths.append((current[0] + 1, current[1]))

    score = {}
    score[start] = 0

    for path in possible_paths:
        can_continue = True
        current = path
        step = 0
        visited = [start]
        visited.append(path)
        while can_continue:
            step +=1
            if current in score.keys():
                if step < score[current]:
                    score[current] = step
                else:
                    can_continue = False
            else:
                score[current] = step
            found = False
            if paths[current] == "|":
                test = (current[0], current[1]-1)
                if test in paths.keys() and test not in visited and paths[test] in up:
                    current = test
                    found = True
                else:
                    test = (current[0], current[1] + 1)
                    if test in paths.keys() and test not in visited and paths[test] in down:
                        current = test
                        found = True
            elif paths[current] == "-":
                test = (current[0]-1, current[1])
                if test in paths.keys() and test not in visited and paths[test] in left:
                    current = test
                    found = True
                else:
                    test = (current[0] + 1, current[1])
                    if test in paths.keys() and test not in visited and paths[test] in right:
                        current = test
                        found = True
            else:
                if paths[current] not in up:
                    test = (current[0], current[1]-1)
                    if test in paths.keys() and test not in visited and paths[test] in up:
                        current = test
                        found = True
                if paths[current] not in down and not found:
                    test = (current[0], current[1] + 1)
                    if test in paths.keys() and test not in visited and paths[test] in down:
                        current = test
                        found = True
                if paths[current] not in left and not found:
                    test = (current[0]-1, current[1])
                    if test in paths.keys() and test not in visited and paths[test] in left:
                        current = test
                        found = True
                if paths[current] not in right and not found:
                    test = (current[0] + 1, current[1])
                    if test in paths.keys() and test not in visited and paths[test] in right:
                        current = test
                        found = True
            if not found:
                can_continue = False

            visited.append(current)

    return score

def part1(data):
    input, start = parse(data)
    goal = traverse(input, start)

    return max(goal.values())

def part2(data):
    input, start = parse(data)
    goal = traverse(input, start)
    
    walls = ["L", "|", "J", "S"]

    total = 0

    for coord in input:
        if coord not in goal.keys():
            count = 0
            for i in range(coord[0]):
                if input[(i, coord[1])] in walls and (i, coord[1]) in goal.keys():
                    count +=1
            if count % 2 == 1:
                total+=1
            

    
    return total

if __name__ == "__main__":
    data = input()
    #print("part 1:", part1(data))
    print("part 2:", part2(data))