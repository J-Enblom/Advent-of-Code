def input():
    with open('input.txt', 'r') as file:
        text = file.read()
        lines = text.split("\n")
    return lines

def parse(data):
    res = []
    for line in data:
        for c in line:
            res.append(int(c))
    return res

def part1(data):
    input = parse(data)
    even = 0
    id = 0
    disk = []
    for n in input:
        if even%2 == 0:
            for i in range(n):
                disk.append(id)
            id += 1
        else:
            for i in range(n):
                disk.append(".")
        even += 1
    arranged = []
    stop = len(disk)-1
    i = 0
    while i <= stop:
        if disk[i] == ".":
            f = stop
            while f > i:
                if disk[f] != ".":
                    arranged.append(disk[f])
                    stop = f-1
                    break
                else:
                    f -= 1

        else:
            arranged.append(disk[i])
        i += 1

    res = 0
    for i in range(len(arranged)):
        res += i* arranged[i]

    return res

def part2(data):
    input = parse(data)
    even = 0
    id = 0
    disk = []
    for n in input:
        if even%2 == 0:
            for i in range(n):
                disk.append(id)
            id += 1
        else:
            for i in range(n):
                disk.append(".")
        even += 1
    block = len(disk)-1

    while 0 <= block:
        if disk[block] != ".":
            file = disk[block]
            c = block - 1
            while disk[c] == file:
                c-=1
            filesize = block - c
            i = 0
            found = False
            while not found:
                if disk[i] == ".":
                    d = i+1
                    while disk[d] == ".":
                        d += 1
                    size = d - i
                    if size >= filesize:
                        for x in range(filesize):
                            disk[i] = file
                            disk[block] = "."
                            i += 1
                            block -= 1
                        found = True
                    else:
                        i = d
                else:
                    i += 1
                    if i > c:
                        found = True
            block = c
        else:
            block -= 1
    res = 0
    for i in range(len(disk)):
        if disk[i] != ".":
            res += i* disk[i]

    return res


if __name__ == "__main__":
    data = input()
    print("part 1:", part1(data))
    print("part 2:", part2(data))