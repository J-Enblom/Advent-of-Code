def input():
    with open('input.txt', 'r') as file:
        text = file.read()
        lines = text.split("\n")
    return lines

def parse(data):
    rules = []
    orders = []
    flag = True
    for line in data:
        if line == "":
            flag = False
            continue
        if flag:
            rules.append(line)
        else:
            orders.append(line.split(","))

    return rules, orders

def part1(data):
    rules, orders = parse(data)
    ruleDict = {}
    for rule in rules:
        r = rule.split("|")
        if r[0] in ruleDict.keys():
            ruleDict[r[0]].append(r[1])
        else:
            ruleDict[r[0]] = [r[1]]
    res = 0
    for order in orders:
        orderBool = True
        for i in range(len(order)-1):
            if not orderBool:
                continue
            flag = True
            for p in range(i+1, len(order)):
                if order[p] not in ruleDict[order[i]]:
                    flag = False
            if not flag:
                orderBool = False
        if orderBool:
            res += int(order[len(order)//2])
    return res

def part2(data):
    rules, orders = parse(data)
    ruleDict = {}
    for rule in rules:
        r = rule.split("|")
        if r[0] in ruleDict.keys():
            ruleDict[r[0]].append(r[1])
        else:
            ruleDict[r[0]] = [r[1]]
    res = 0
    incOrders = []
    for order in orders:
        orderBool = True
        for i in range(len(order)-1):
            if not orderBool:
                continue
            for p in range(i+1, len(order)):
                if order[i] not in ruleDict.keys() or order[p] not in ruleDict[order[i]]:
                    orderBool = False
        if not orderBool:
            incOrders.append(order)
    for order in incOrders:
        newOrders = []
        for i in range(len(order)):
            newOrder = [order[i]]
            for p in range(len(order)):
                if order[i] in ruleDict.keys() and order[p] in ruleDict[order[i]]:
                    newOrder.append(order[p])
            newOrders.append(newOrder)
        newOrders.sort(key=len)
        res += int(newOrders[len(newOrders)//2][0])

    '''        
    for order in incOrders:
        newOrder = order
        for i in range(len(order)):
            newOrder = updatePos(newOrder, i, ruleDict)
        res += int(newOrder[len(newOrder)//2])
    '''

    return res

def updatePos(order, start, ruleDict):
    swap = 0
    for p in range(start+1, len(order)):
        if order[start] not in ruleDict.keys() or order[p] not in ruleDict[order[start]]:
            swap += 1
        else:
            break
    save = order[start]
    for x in range(swap):
        order[start+x] = order[start+x+1]
    order[start+swap] = save
    if swap > 1:
        order = updatePos(order, start+1, ruleDict)
    return order


if __name__ == "__main__":
    data = input()
    print("part 1:", part1(data))
    print("part 2:", part2(data))