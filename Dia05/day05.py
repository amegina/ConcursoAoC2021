import re


def parse():
    with open("./input.txt", 'r') as file:
        return [[int(n) for n in re.findall('[0-9]+', i.strip())] for i in file]


def addPoint(p):
    if p not in map.keys():
        map[p] = 1
    else:
        map[p] += 1


def diagonal(line, deltaX, deltaY):
    while(line[:2] != line[2:]):
        addPoint((line[0],line[1]))
        line[0] += deltaX
        line[1] += deltaY
    addPoint((line[0], line[1]))



segments = parse()
map = {}

for s in segments:
    if s[0] == s[2]:
        diagonal(s, 0, 1 if s[3] > s[1] else -1)
    elif s[1] == s[3]:
        diagonal(s, 1 if s[2] > s[0] else -1, 0)

print("Star1:", len([x for x in map.values() if x > 1]))

for s in segments:
    if s[0] != s[2] and s[1] != s[3]:
        diagonal(s, 1 if s[2] > s[0] else -1, 1 if s[3] > s[1] else -1)

print("Star2:", len([x for x in map.values() if x > 1]))