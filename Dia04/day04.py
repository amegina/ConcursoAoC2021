def parse():
    with open("./input.txt", 'r') as file:
        nums = [int(i) for i in file.readline().split(',')]
        lines = [[int(num) for num in line.strip().split(' ') if num != ''] for line in file if len(line) > 1]
        return nums, [lines[i:i + 5] for i in range(0, len(lines), 5)]


def rows(mat):
    return min([max([n.index(e) for e in r]) for r in mat])


def score(pos, board):
    s = 0
    for row in m[board]:
        for e in row:
            if n.index(e) > pos:
                s += e
    return s * n[pos]


p = parse()
n = p[0]
m = p[1]

best = [len(n), 0]
worse = [0, 0]

for idx, b in enumerate(m):
    val = min(rows(b), rows([*zip(*b)]))
    if val < best[0]:
        best[0] = val
        best[1] = idx
    if val > worse[0]:
        worse[0] = val
        worse[1] = idx

print("Star1:", score(best[0], best[1]))
print("Star2:", score(worse[0], worse[1]))
