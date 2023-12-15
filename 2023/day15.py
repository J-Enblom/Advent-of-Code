def input():
    with open('input.txt', 'r') as file:
        text = file.read()
        lines = text.split(",")
    return lines

def parse(data):
    res = []
    for line in data:
        res.append(line)
    return res

def part1(data):
    input = parse(data)
    total = 0
    for s in input:
        s_value = 0
        for char in s:
            s_value += ord(char)
            s_value *= 17
            s_value = s_value%256
        total +=s_value
    return total

def part2(data):
    input = parse(data)
    total = 0
    hashm = {}
    for s in input:
        equal = True
        if "=" in s:
            s = s.split("=")
        else:
            s = s.split("-")
            equal = False
        s_value = 0
        for char in s[0]:
            s_value += ord(char)
            s_value *= 17
            s_value = s_value%256


        if equal:
            if s_value in hashm.keys():
                found = False
                for stored in range(len(hashm[s_value])):
                    if hashm[s_value][stored][0] == s[0]:
                        hashm[s_value][stored][1] = s[1]
                        found = True
                        break
                if not found:
                    hashm[s_value].append(s)
            else:
                hashm[s_value] = [s]
        else:
            if s_value in hashm.keys():
                for c in range(len(hashm[s_value])):
                    if hashm[s_value][c][0] == s[0]:
                        hashm[s_value].pop(c)
                        break
    for box in hashm.keys():
        slot = 1
        for focal in hashm[box]:
            total += ((int(box)+1) * slot * int(focal[1]))
            slot += 1

    return total

if __name__ == "__main__":
    data = input()
    print("part 1:", part1(data))
    print("part 2:", part2(data))