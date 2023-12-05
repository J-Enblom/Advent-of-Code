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
    conversion = "stop"
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


def fill_map(dict, key, start, ranges):
    result = []
    length = len(start)
    search = []
    new_key = "stop"
    for keys in dict.keys():
        if key == keys[0]:
            search = dict[keys]
            new_key = keys[0]
            break
    search.sort(key = lambda x: x[1])
        
    for i in range(length):
        s = start[i]
        e = ranges[i] + s
        
        while s != e :
            for m in search:
                if s >= m[1] and s < m[1] + m[2]:
                    if (e > m[2] + m[1]):
                        result.append((s, new_key, m[2] - (s-m[1])))
                        s += m[2] - (s-m[1])
            result.append((s, new_key, e - s))
            s = e
            
            

    return result

def part2(data):
    dict = parse(data)
    current = "seed"
    goal = "stop"
    final = []
    ranges = []
    seeds = []
    for num in range(len(dict["seeds"])):
        if num%2 == 0:
            seeds.append(dict["seeds"][num])
        else:
            ranges.append(dict["seeds"][num])
    seeds = fill_map(dict, "seed", seeds, ranges)
    while len(seeds)> 0:
        curr = seeds.pop(0)
        if curr[1] == goal:
            final.append(curr[0])
        else:
            seed, current = convert(dict, curr[0], curr[1])
            seeds += fill_map(dict, current, [seed], [curr[2]])


    return min(final)

if __name__ == "__main__":
    data = input()
    print("part 1:", part1(data))
    print("part 2:", part2(data))