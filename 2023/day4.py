def input():
    with open('input.txt', 'r') as file:
        text = file.read()
        lines = text.split("\n")
    return lines

def parse(data):
    cards = []
    winning = []

    for line in data:
        split_line = line.split(":")[1].split("|")
        cards.append(split_line[0].split())
        winning.append(split_line[1].split())

    return cards, winning

def part1(data):
    cards, winning = parse(data)
    total = 0

    for card in range(len(cards)):
        count = -1
        for number in cards[card]:
            if number in winning[card]:
                count += 1
        if count >= 0:
            total += 2 ** (count)

    return total

def part2(data):
    cards, winning = parse(data)
    total = 0
    amount = {}

    for card in range(len(cards)):
        count = 0
        copy = 0
        original = 1
        if card in amount.keys():
            copy = amount[card]
        
        for number in cards[card]:
            
            if number in winning[card]:
                count += 1
                index = card + count
                current = amount[index] if index in amount.keys() else 0
                amount[index] = current + original + copy

        total += original + copy

    return total

if __name__ == "__main__":
    data = input()
    print("part 1:", part1(data))
    print("part 2:", part2(data))