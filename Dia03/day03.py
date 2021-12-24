def lines():
    with open('./input.txt', 'r') as file:
        return [[int(j) for j in i.strip()] for i in file]


def common(elements):
    dic = {0: 0, 1: 0}
    for e in elements:
        dic[e] += 1
    if dic[0] > dic[1]:
        return 0
    elif dic[0] < dic[1]:
        return 1
    else:
        return 2


data = lines()

bin1 = [str(common(bits)) for bits in [*zip(*data)]]
bin2 = ['1' if b == '0' else '0' for b in bin1]

print("Star1:", int(''.join(bin1), 2) * int(''.join(bin2), 2))

o2 = lines()
co2 = lines()

idx = 0
while len(o2) > 1:
    c = common([*zip(*o2)][idx])
    if c == 2:
        c = 1
    o2 = [num for num in o2 if num[idx] == c]
    idx += 1

idx = 0
while len(co2) > 1:
    c = 1 - common([*zip(*co2)][idx])
    if c == -1:
        c = 0
    co2 = [num for num in co2 if num[idx] == c]
    idx += 1

print("Star2:", int(''.join([str(x) for x in o2[0]]), 2) * int(''.join([str(x) for x in co2[0]]), 2))
