def parse():
    with open('./input.txt', 'r') as file:
        start = file.readline().strip()
        file.readline()
        dic = {}
        blank = {}
        for line in file:
            (cause, effect) = line.strip().split(" -> ")
            dic[cause] = effect
            blank[cause] = 0
        return start, dic, blank


def solve(iterations):
    for n in range(iterations):
        pend = []
        for v in [e for e in values.keys() if values[e] > 0]:
            pend.append((v[0] + pairs[v], values[v]))
            pend.append((pairs[v] + v[1], values[v]))
            values[v] = 0
        for v in pend:
            values[v[0]] += v[1]

    sol = {}
    for v in values.keys():
        if v[0] in sol:
            sol[v[0]] += values[v]
        else:
            sol[v[0]] = values[v]
        if v[1] in sol:
            sol[v[1]] += values[v]
        else:
            sol[v[1]] = values[v]
    sol[ini] += 1
    sol[fin] += 1

    return int(sol[max(sol, key=sol.get)] / 2 - sol[min(sol, key=sol.get)] / 2)


(template, pairs, values) = parse()

ini = template[0]
fin = template[-1]

for i in range(len(template) - 1):
    values[template[i:i + 2]] += 1

print("Star1:", solve(10))
print("Star2:", solve(30))
