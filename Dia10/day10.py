def parse():
    with open('./input.txt', 'r') as file:
        return [i.strip() for i in file]


def check(line):
    stack = []
    for car in line:
        if car in comp.keys():
            stack.append(comp[car])
        elif stack[-1] == car:
            stack.pop()
        else:
            return valueC[car]
    return stack


lines = parse()
corrupted = 0
comp = {'(': ')', '[': ']', '{': '}', '<': '>'}
valueC = {')': 3, ']': 57, '}': 1197, '>': 25137}
valueI = {')': 1, ']': 2, '}': 3, '>': 4}

err = 0
scores = []
for ln in lines:
    ret = check(ln)
    if type(ret) == int:
        err += ret
    else:
        score = 0
        while ret:
            score *= 5
            score += valueI[ret.pop()]
        scores.append(score)
scores.sort()

print("Star1:", err)
print("Star2:", scores[int(len(scores) / 2)])
