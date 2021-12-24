def lines():
    with open('./input.txt', 'r') as file:
        return [i.strip() for i in file]


lines = lines()

dic = {'f': 0, 'f2': 0, 'd': 0, 'u': 0}
for line in lines:
    if line[0] == 'f':
        dic['f2'] += (dic['d'] - dic['u']) * int(line[-1])
    dic[line[0]] += int(line[-1])

x = dic['f']
y1 = dic['d'] - dic['u']
y2 = dic['f2']

print("Star1:", x * y1)
print("Star2:", x * y2)
