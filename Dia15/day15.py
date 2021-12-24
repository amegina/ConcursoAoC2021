from queue import PriorityQueue


def parse():
    with open('./input.txt', 'r') as file:
        mat = []
        for line in file:
            mat.append([int(e) for e in line.strip()])
        return mat


def solve(mat):
    pq = PriorityQueue()
    target = (len(mat) - 1, len(mat[0]) - 1)
    delta = [1, 0, -1, 0]

    (pred, risk, p) = (len(mat) + len(mat[0]) - 2, 0, (0, 0))
    visited = set()
    while p != target:
        visited.add(p)
        for d in range(4):
            newP = (p[0] + delta[d - 1], p[1] + delta[d])
            if newP not in visited and 0 <= newP[0] <= target[0] and 0 <= newP[1] <= target[1]:
                pq.put((risk + mat[newP[0]][newP[1]] + target[0] + target[1] - newP[0] - newP[1],
                        risk + mat[newP[0]][newP[1]], newP))
        (pred, risk, p) = pq.get()
        while p in visited:
            (pred, risk, p) = pq.get()
    return risk


m = parse()
print("Star1:", solve(m))

x = len(m[0])
y = len(m)
for i in range(4):
    m += [[((e + i) % 9) + 1 for e in r] for r in m[:y]]
for r in m:
    for i in range(4):
        r += [((e + i) % 9) + 1 for e in r[:x]]

print("Star2:", solve(m))
