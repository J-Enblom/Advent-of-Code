def input():
    with open('input.txt', 'r') as file:
        text = file.read()
        lines = text.split("\n")
    return lines

def parse(data):
    res = []
    for line in data:
        res.append([int(x) for x in line.split()])

    return res

def rec_finder(seq):
    i = 0
    differences = []
    while i < len(seq) - 1:
        differences.append(seq[i+1]- seq[i])
        i += 1
    if all(v == 0 for v in differences):
        return seq[-1], seq[0]
    dif_l, dif_f = rec_finder(differences)
    last = seq[-1] + dif_l
    first = seq[0] - dif_f
    return last, first

def solve(data):
    input = parse(data)
    total_last = 0
    total_first = 0
    for seq in input:
        last, first = rec_finder(seq)
        total_last += last
        total_first += first
    return total_last, total_first

if __name__ == "__main__":
    data = input()
    part1, part2 = solve(data)
    print("part 1:", part1)
    print("part 2:", part2)