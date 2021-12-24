def parse():
    with open('./input.txt', 'r') as file:
        dic = {}
        i = 0
        for line in file:
            j = 0
            for number in line.strip():
                dic[(j, i)] = int(number)
                j += 1
            i += 1
        return dic


delta = [0, 1, 1, 1, 0, -1, -1, -1]


def flash(flashed, p):
    if p in flashed:
        return

    levels[p] += 1

    if levels[p] > 9:
        flashed.append(p)
        for i in range(8):
            adj = (p[0] + delta[i], p[1] + delta[i-2])
            if adj in levels.keys():
                flash(flashed, adj)
        levels[p] = 0

    return


levels = parse()
count = 0
sync = -1
for step in range(100):
    mem = []
    for point in levels.keys():
        flash(mem, point)
    numFlash = len(mem)
    count += numFlash
    if numFlash == len(levels.keys()) and sync == -1:
        sync = step

print("Star1:", count)

step = 100
while sync == -1:
    mem = []
    for point in levels.keys():
        flash(mem, point)
    numFlash = len(mem)
    if numFlash == len(levels.keys()) and sync == -1:
        sync = step + 1
    step += 1

print("Star2:", sync)
