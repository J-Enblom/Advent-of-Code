def input():
    with open('input.txt', 'r') as file:
        text = file.read()
        lines = text.split("\n")
    return lines

def parse(data):
    result = []
    for line in data:
        result.append(line.split(":")[1].split())
    return result

def part1(data):
    total = 1
    input = parse(data)
    for race in range(len(input[0])):
        amount = 0
        for hold in range(int(input[0][race])):
            if hold * (int(input[0][race])-hold) > int(input[1][race]):
                amount+=1
        if amount > 0:
            total *= amount
    return total

def parse2(data):
    result = []
    for line in data:
        string = ""
        for x in line:
            if x.isdigit():
                string += x
        result.append(int(string))
    return result


def part2(data):
    input = parse2(data)
    amount = 0
    for i in range(input[0]):
        if i * (input[0]-i) > input[1]:
            amount += 1
    return amount

if __name__ == "__main__":
    data = input()
    print("part 1:", part1(data))
    print("part 2:", part2(data))