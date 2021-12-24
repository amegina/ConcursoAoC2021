def parse():
    with open('./input.txt', 'r') as file:
        dic = {}
        i = 0
        for line in file:
            j = 0
            for number in line.strip():
                dic[(j, i)] = number
                j += 1
            i += 1
        return dic


heights = parse()

risk = 0
low = []
for point in heights.keys():
    less = 0
    value = heights[point]
    delta = [0, 1, 0, -1]
    for d in range(4):
        try:
            if heights[(point[0] + delta[d], point[1] + delta[d - 1])] > value:
                less += 1
            else:
                break
        except KeyError:
            less += 1
    if less == 4:
        risk += int(value) + 1
        low.append(point)


def visit(p, visited):
    if p in visited or heights[p] == '9':
        return 0
    else:
        visited.append(p)

    count = 0
    for i in range(4):
        try:
            count += visit((p[0] + delta[i], p[1] + delta[i - 1]), visited)
        except KeyError:
            pass
    return count + 1


basins = []
for point in low:
    basins.append(visit(point, []))
basins.sort(reverse=True)

print("Star1:", risk)
print("Star2:", basins[0] * basins[1] * basins[2])
