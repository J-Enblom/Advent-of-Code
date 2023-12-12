import copy
from functools import cache

def input():
    with open('input.txt', 'r') as file:
        text = file.read()
        lines = text.split("\n")
    return lines

def parse(data):
    res = []
    for line in data:
        res.append(line.split())
    return res

@cache
def rec_check(a, b):
    row = copy.deepcopy(a)
    mistakes = copy.deepcopy(b)
    
    if row == "" and mistakes or row == "." and mistakes:
        return 0

    if not mistakes:
        if row.count("#") == 0:
            return 1
        return 0
    
    check = row[0]
    if check == ".":            
        return rec_check(row[1:], mistakes)
    elif check == "?":
        count = rec_check("." + row[1:], mistakes)
        count += rec_check("#" + row[1:], mistakes)
        return count
    else:
        mistake = mistakes[0]
        mistakes = mistakes[1:]
        if mistake > len(row):
            return 0
        if row[:mistake].count(".") != 0:
            return 0
        if len(row[mistake:]) > 0:
            if row[mistake] == "#":
                return 0
            if row[mistake] == "?":
                if len (row[mistake:]) > 1:
                    return rec_check("." + row[mistake + 1:], mistakes)
                return rec_check(".", mistakes)
            return rec_check(row[mistake:], mistakes)
        return rec_check("", mistakes)



def arrangments(record):
    condition = record[0]
    damaged =tuple([int(n) for n in record[1].split(",")])
    print(damaged)

    count = rec_check(condition, damaged)

    return count

def part1(data):
    input = parse(data)
    total = 0
    for record in input:
        total += arrangments(record)
    return total

def part2(data):
    input = parse(data)
    total = 0
    for record in input:
        mistakes = (record[1] + ",") * 5
        mistakes = mistakes[:-1]
        condition = record[0]
        for i in range(4):
            condition = condition + "?" + record[0]
            

        total += arrangments((condition, mistakes))
    return total

if __name__ == "__main__":
    data = input()
    #print("part 1:", part1(data))
    print("part 2:", part2(data))