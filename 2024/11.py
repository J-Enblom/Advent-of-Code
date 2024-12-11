def input():
    with open('input.txt', 'r') as file:
        text = file.read()
        lines = text.split("\n")
    return lines

def parse(data):
    res = []
    for line in data:
        for c in line.split():
            res.append(c)
    return res

RES = [0]

def iterate(stones, i, r):
    if i >= r:
        for key in stones.keys():
            RES[0] += stones[key]
    else:
        n_stones = {}
        i += 1
        for stone in stones.keys():
            size = len(stone)
            amount = stones[stone]
            if stone == "0":
                n = "1"
            elif size%2 == 0:
                left = str(int(stone[0:size//2]))
                n = str(int(stone[size//2:]))
                if left not in n_stones.keys():
                    n_stones[left] = amount
                else:
                    n_stones[left] += amount
            else:
                n = str(int(stone)*2024)
            if n not in n_stones.keys():
                n_stones[n] = amount
            else:
                n_stones[n] += amount
        iterate(n_stones, i, r)


def solve(data, r):
    input = parse(data)
    for c in input: 
        stone = {c:1}
        iterate(stone, 0, r)
        
    return RES[0]


if __name__ == "__main__":
    data = input()
    print("part 1:", solve(data, 25))
    RES[0] = 0
    print("part 2:", solve(data, 75))