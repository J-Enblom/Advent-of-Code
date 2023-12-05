def input():
    with open('input.txt', 'r') as file:
        text = file.read()
        lines = text.split("\n")
    return lines

def part1(data):
    symbols = []
    total = 0
    for line in data:
        symbols.append(list(line))

    for y in range(len(symbols)):
        x = 0
        while x < len(symbols[y]):
            current = symbols[y][x]
            if current.isdigit():
                top = max(y-1, 0)
                bottom = min(y+1, len(symbols))
                left = max(x-1,0)

                while x+1< len(symbols[y]):
                    if (symbols[y][x+1].isdigit()):
                        x += 1
                        current += symbols[y][x]
                    else:
                        break
                
                right = min(x+2, len(symbols))
                col_amount = symbols[top:bottom+1]
                res = []
                for col in col_amount:
                    res += col[left:right]
                check = False
                for symbol in res:
                    if check:
                        break
                    if symbol != "." and not symbol.isdigit():
                        total += int(current)
                        check = True
            x += 1
                
    return total

def part2(data):
    symbols = []
    total = 0
    for line in data:
        symbols.append(list(line))
    for y in range(len(symbols)):
        for x in range(len(symbols[y])):
            current = symbols[y][x]
            if current == "*":
                top = max(y-1, 0)
                bottom = min(y+1, len(symbols))
                left = max(x-3,0)
                right = min(x+3, len(symbols))
                col_amount = symbols[top:bottom+1]
                res = []
                for col in col_amount:
                    res.append(col[left:right+1])
                numbers = []
                for ny in range (0,3):
                    for nx in range(2, 5):
                        n = ""
                        digit = res[ny][nx]
                        if digit.isdigit():
                            n = digit
                            if res[ny][nx-1].isdigit():
                                n = res[ny][nx-1] + n
                                if nx < len(res[ny]) and res[ny][nx+1].isdigit():
                                    n += res[ny][nx+1]
                                elif res[ny][nx-2].isdigit():
                                    n = res[ny][nx-2] + n
                            else:
                                if nx+1 < len(res[ny]) and res[ny][nx+1].isdigit():
                                    n += res[ny][nx+1]
                                    if nx+2 < len(res[ny]) and res[ny][nx+2].isdigit():
                                        n += res[ny][nx+2]
                            if n not in numbers:
                                numbers.append(n)
                if len(numbers )>1:
                    total += int(numbers[0]) * int(numbers[-1])
    return total



if __name__ == "__main__":
    data = input()
    print("part 1:", part1(data))
    print("part 2:", part2(data))