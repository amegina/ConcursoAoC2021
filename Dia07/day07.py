def parse():
    with open("./input.txt", 'r') as file:
        return [int(x) for x in file.readline().split(",")]


def cost(costFunc, idx):
    return sum([costFunc(x, idx) for x in nums])


def linear(num, idx):
    return abs(num - idx)


def gauss(num, idx):
    n = linear(num, idx)
    return int(n * (n+1) / 2)


def solve(costFunc):
    bestScore = cost(costFunc, 0)

    for i in range(max(nums) + 1):
        score = cost(costFunc, i)
        if score < bestScore:
            bestScore = score

    return bestScore


nums = parse()

print("Star1:", solve(linear))
print("Star2:", solve(gauss))
