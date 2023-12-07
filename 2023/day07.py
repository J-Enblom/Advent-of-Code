def input():
    with open('input.txt', 'r') as file:
        text = file.read()
        lines = text.split("\n")
    return lines

def parse(data):
    result = []
    for line in data:
        result.append((line.split()[0], line.split()[1]))
    return result

def sort_hand(card):
    dressed_cards = {
        "A" : 14,
        "K" : 13,
        "Q" : 12,
        #"J" : 11,
        "T" : 10,
        "J" : 1
    }
    if card.isdigit():
        return int(card)
    else:
        return dressed_cards[card]

def sort_hands(hands):


    five_of = []
    four_of = []
    full_house = []
    three_of = []
    two_pair = []
    one_pair = []
    high_card = []

    for hand in hands:
        current = []
        bonus = hand[0].count("J")
        for card in hand[0]:
            current.append((card, (hand[0].count(card)))) if (card, (hand[0].count(card))) not in current and card != "J" else current
        current.sort(key=lambda x: x[1], reverse=True)
        print(current)
        i = 0
        found = False
        if len(current) == 0:
            five_of.append(hand)
            found = True
        while i != len(current):
            if current[i][1] + bonus == 5:
                five_of.append(hand)
                found = True
                break
            elif current[i][1] + bonus == 4:
                four_of.append(hand)
                found = True
                break
            elif current[i][1] + bonus == 3:
                for x in range(i + 1, len(current)-i):
                    if current[x][1] >= 2:
                        full_house.append(hand)
                        found = True
                        break
                if not found:
                    three_of.append(hand)
                    found = True
                break
            elif current[i][1] + bonus == 2:
                for x in range(i + 1, len(current)-i):
                    if current[x][1] > 1:
                        two_pair.append(hand)
                        found = True
                        break
                if not found:
                    one_pair.append(hand)
                    found = True
                break
            i += 1
        if not found:
            high_card.append(hand)

    result = [high_card, one_pair, two_pair, three_of, full_house, four_of, five_of]
    for hand in result:
        hand.sort(key= lambda x: (sort_hand(x[0][0]), sort_hand(x[0][1]), sort_hand(x[0][2]), sort_hand(x[0][3]), sort_hand(x[0][4])))

    print(high_card)
    return result




def part1(data):
    input = parse(data)
    res = sort_hands(input)
    number = 1
    total = 0
    for hand_type in res:
        print(len(hand_type))
        for hand in hand_type:
            total += int(hand[1])*number
            number +=1
    return total

def part2(data):
    return None

if __name__ == "__main__":
    data = input()
    print("part 1:", part1(data))
    print("part 2:", part2(data))