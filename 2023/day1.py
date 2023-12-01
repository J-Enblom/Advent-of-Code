import re

def input():
    with open('input.txt', 'r') as file:
        text = file.read()
        lines = text.split("\n")
    return lines

def part1(data):
    total = 0
    for line in data:
        res = [int(num) for num in re.findall(r"\d+", line)]
        if len(res) > 0:
            firstDigit = int(str(res[0])[:1])
            secondDigit = res[-1]%10
            total += firstDigit*10 + secondDigit

    return total

help_dict = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'zero': 0,
    "1":1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9

}
 
def part2(data):
    total = 0
    for line in data:
        res = [(help_dict[x], line.find(x)) for x in help_dict.keys() if line.find(x) >-1]
        right_res = set([(help_dict[x], line.rfind(x)) for x in help_dict.keys() if line.rfind(x) >-1]) - set(res)
        res += list(right_res)
        res.sort(key = lambda x: x[1])
        if len(res) > 0:
            line_tot = res[0][0]*10 + res[-1][0]
            total += line_tot


    return total

if __name__ == "__main__":
    data = input()
    print("part 1:", part1(data))
    print("part 2:", part2(data))
