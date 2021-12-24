def parse():
    with open('./input.txt', 'r') as file:
        dic = {}
        for line in file:
            if line.strip() == "":
                break
            (x, y) = line.strip().split(',')
            dic[(int(x), int(y))] = '#'
        x = []
        y = []
        for line in file:
            (coord, val) = line.strip().split('=')
            if coord[-1] == 'x':
                x.append(int(val))
            else:
                y.append(int(val))
        return dic, x, y


def solve(dots, x, y):
    for i in x:
        keys = [e for e in dots.keys()]
        for d in keys:
            if i < d[0]:
                new = (2 * i - d[0], d[1])
                dots.pop(d)
                dots[new] = '#'
    for i in y:
        keys = [e for e in dots.keys()]
        for d in keys:
            if i < d[1]:
                new = (d[0], 2 * i - d[1])
                dots.pop(d)
                dots[new] = '#'
    return len(dots.keys()), dots


def draw(dots):
    for y in range(6):
        for x in range(40):
            if (x, y) in dots.keys():
                print('#', end='')
            else:
                print(' ', end='')
        print()


(paper, xFold, yFold) = parse()
print("Star1:", solve(paper, [xFold[0]], [])[0])
print("Star2:")
draw(solve(paper, xFold, yFold)[1])
