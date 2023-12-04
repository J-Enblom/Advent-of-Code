def input():
    with open('input.txt', 'r') as file:
        text = file.read()
        lines = text.split("\n")
    return lines

def part1(data):
    cards = []
    winning = []
    for line in data:
        cards.append(line.split(":")[1].split("|")[0].split(" "))
        winning.append(line.split(":")[1].split("|")[1].split(" "))
    
    total = 0
    for card in range(len(cards)):
        first = True
        score = 0
        for number in cards[card]:
            if number.isdigit() and number in winning[card]:
                if first:
                    score +=1
                    first = False
                else:
                    score *=2
        total += score

    return total

def part2(data):
    cards = []
    winning = []
    for line in data:
        cards.append(line.split(":")[1].split("|")[0].split(" "))
        winning.append(line.split(":")[1].split("|")[1].split(" "))
    
    total = 0
    amount = {}
    for card in range(len(cards)):
        count = 0
        copy = 0
        original = 1
        if card in amount.keys():
                copy = amount[card]
        
        for number in cards[card]:
            
            if number.isdigit() and number in winning[card]:
                count += 1
                index = card + count
                if index in amount.keys():
                    current = amount[index]
                    amount[index] = current + original + copy
                else:
                    amount[index] = original + copy

        total += original + copy

    return total

if __name__ == "__main__":
    data = input()
    print("part 1:", part1(data))
    print("part 2:", part2(data))