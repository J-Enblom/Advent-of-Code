def input():
    with open('input.txt', 'r') as file:
        text = file.read()
        lines = text.split("\n")
    return lines  

def solution(data):
    max_shards = {"red":12,"green":13, "blue":14}
    total_1 = 0
    total_2 = 0

    for line in data:
        min_shards={"red": 0, "blue": 0, "green": 0}
        valid = True
        first_split = line.split(":")
        index = [int(s) for s in first_split[0].split() if s.isdigit()][0]
        split_game = first_split[1].split(";")
        for i in split_game:
            split_shard = i.split(",")
            for shard in split_shard:
                amount, color = shard.split()
                if int(amount) > max_shards[color]:
                    valid = False
                if int(amount) > min_shards[color]:
                    min_shards[color] = int(amount)
        
        if valid:
            total_1+=index
        sum = 1
        for key in min_shards.keys():
            sum*=min_shards[key]
        total_2+= sum
                
    return total_1, total_2

if __name__ == "__main__":
    data = input()
    result1, result2 = solution(data)
    print("part 1:", result1)
    print("part 2:", result2)