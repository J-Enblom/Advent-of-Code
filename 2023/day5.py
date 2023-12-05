def input():
    with open('input.txt', 'r') as file:
        text = file.read()
        lines = text.split("\n")
    return lines

def parse(data):
    dic_map = {}
    start = data[0].split(":")
    dic_map[start[0]] = []
    for seed in start[1].split():
        dic_map[start[0]].append(int(seed))
    data = data[2:]
    new_conversion = True
    keys = ""
    for line in data:
        if new_conversion:
            split = line.split("-to-")
            keys = (split[0],split[1].split(" ")[0])
            dic_map[keys] = []
            new_conversion = False
        elif line == "":
            new_conversion = True
        else:
            dic_map[keys].append([int(x) for x in line.split()])

    return dic_map

def convert(dict, number, current):
    conversion = ""
    con_map = []
    for key in dict.keys():
        if key[0] == current:
            conversion = key[1]
            con_map = dict[key]
            
    for mapping in con_map:
        if number >= mapping[1] and number < mapping[1] + mapping[2]:
            if mapping[0] > mapping[1]:
                number += mapping[0] - mapping[1]
            else:
                number -= mapping[1] - mapping[0]
            break

    return number, conversion

def part1(data):
    dict = parse(data)
    current = "seed"
    goal = "location"
    final = []
    for seed in dict["seeds"]:
        while current != goal:
            seed, current = convert(dict, seed, current)
        current = "seed"
        final.append(seed)

    return min(final)




def part2(data):
    dict = parse(data)
    current = "seed"
    goal = "location"
    final = []
    ranges = []
    seeds = []
    for num in range(len(dict["seeds"])):
        if num%2 == 0:
            seeds.append(dict["seeds"][num])
        else:
            ranges.append(dict["seeds"][num])
    visited = {}
    for key in dict.keys():
        if key != "seeds":
            visited[key[1]] = []
    visited["seed"] = [] #8:42
        
    for i in range(len(seeds)):
        for r in range(ranges[i]):
            seed = seeds[i] + r
            while current != goal:
                if seed in visited[current]:
                    break
                visited[current].append(seed)
                seed, current = convert(dict, seed, current)
            if current == goal:
                final.append(seed)
            current = "seed"
            

    return min(final)

if __name__ == "__main__":
    data = input()
    print("part 1:", part1(data))
    print("part 2:", part2(data))