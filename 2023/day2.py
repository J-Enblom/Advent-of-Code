def input():
    with open('input.txt', 'r') as file:
        text = file.read()
        lines = text.split("\n")
    return lines

def part1(data):
    max_shards = {"red":12,"green":13, "blue":14}

    total = 0
    for line in data:
        valid = True
        first_split = line.split(":")
        index = [int(s) for s in first_split[0].split() if s.isdigit()][0]
        split_game = first_split[1].split(";")
        for i in split_game:
            split_shard = i.split(",")
            for shard in split_shard:
                if int(shard.split()[0]) > max_shards[shard.split()[1]]:
                    valid = False
        
        if valid:
            total+=index

                
    return total

def part2(data):

    total = 0
    for line in data:
        min_shards={"red": 0, "blue": 0, "green": 0}

        first_split = line.split(":")
        split_game = first_split[1].split(";")
        for i in split_game:
            split_shard = i.split(",")
            for shard in split_shard:
                if int(shard.split()[0]) > min_shards[shard.split()[1]]:
                    min_shards[shard.split()[1]] = int(shard.split()[0])
        
        sum = 1
        for key in min_shards.keys():
            sum*=min_shards[key]
        total+= sum

                
    return total

if __name__ == "__main__":
    data = input()
    print("part 1:", part1(data))
    print("part 2:", part2(data))