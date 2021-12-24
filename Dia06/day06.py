def parse():
    with open("./input.txt", 'r') as file:
        start = [0] * 9
        for i in file.readline().split(","):
            start[int(i)] += 1
        return start


def grow(days):
    for i in range(days):
        born = lantern[0]
        lantern[:-1] = lantern[1:]
        lantern[6] += born
        lantern[8] = born
    return sum(lantern)


lantern = parse()

print("Star1:", grow(80))
print("Star2:", grow(176))
