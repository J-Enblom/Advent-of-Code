def input():
    with open('input.txt', 'r') as file:
        text = file.read()
        lines = text.split("\n")
    return lines

def part1(data):
    card = []
    winning = []
    for line in data:
        card.append(line.split(":")[1].split("|")[0].split(" "))
        winning.append(line.split(":")[1].split("|")[1].split(" "))
    
    total = 0
    for x in range(len(card)):
        first = True
        score = 0
        for number in card[x]:
            if number.isdigit() and number in winning[x]:
                if first:
                    score +=1
                    first = False
                else:
                    score *=2
        total +=score

    return total

def part2(data):
    card = []
    winning = []
    for line in data:
        card.append(line.split(":")[1].split("|")[0].split(" "))
        winning.append(line.split(":")[1].split("|")[1].split(" "))
    
    total = 0
    amount = {}
    for x in range(len(card)):
        count = 0
        copy = 0
        if x in amount.keys():
                copy = amount[x]
        
        for number in card[x]:
            
            if number.isdigit() and number in winning[x]:
                count += 1
                if x + count in amount.keys():
                    current = amount[x + count]
                    amount[x + count] = current + 1 + copy
                else:
                    amount[x + count] = 1 + copy

        total += copy + 1

    return total

if __name__ == "__main__":
    data = input()
    print("part 1:", part1(data))
    print("part 2:", part2(data))