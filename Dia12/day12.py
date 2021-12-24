def parse():
    with open('./input.txt', 'r') as file:
        dic = {}
        for line in file:
            (start, end) = line.strip().split("-")
            add(dic, start, end)
            add(dic, end, start)
        return dic


def add(dic, p1, p2):
    if p1 in dic.keys():
        dic[p1].append(p2)
    else:
        dic[p1] = [p2]


def search(node, visited):
    if node == 'end':
        return 1

    paths = 0
    cond = node[0].islower()
    if cond:
        visited.append(node)
    for p in conn[node]:
        if p not in visited:
            paths += search(p, visited)
    if cond:
        visited.remove(node)

    return paths


def search2(node, visited, single):
    if node == 'end':
        return 1

    paths = 0
    cond = node[0].islower()
    if cond:
        visited.append(node)
    for p in conn[node]:
        if p not in visited:
            paths += search2(p, visited, single)
        elif not single and p != 'start':
            paths += search2(p, visited, True)
    if cond:
        visited.remove(node)

    return paths


conn = parse()
print("Star1:", search('start', []))
print("Star2:", search2('start', [], False))
