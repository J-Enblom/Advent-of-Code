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

def part1(data):
    input = parse(data)
    res = 0
    for protocol in input:
        flag = True
        dec = False
        inc = False
        for i in range(len(protocol)-1):
            change = protocol[i]-protocol[i+1]
            
            if i == 0 and change < 0:
                dec = True
            elif i == 0 and change >= 0:
                inc = True
            if inc:
                if change < 1 or change > 3:
                    flag = False
                    break
            if dec:
                if change > -1 or change < -3:
                    flag = False
                    break
        if flag:
            res += 1

    return res

def part2(data):
    input = parse(data)
    res = 0
    for protocol in input:
        for x in range(len(protocol)):
            prot = protocol[:x] + protocol[x+1:]
            if stupid(prot):
                res +=1
                print(protocol, prot)
                break

    return res

def stupid(protocol):
    flag = True
    dec = False
    inc = False
    for i in range(len(protocol)-1):
        change = protocol[i]-protocol[i+1]
        
        if i == 0 and change < 0:
            dec = True
        elif i == 0 and change >= 0:
            inc = True
        if inc:
            if change < 1 or change > 3:
                flag = False
                break
        if dec:
            if change > -1 or change < -3:
                flag = False
                break
    return flag


if __name__ == "__main__":
    data = input()
    #print("part 1:", part1(data))
    print("part 2:", part2(data))