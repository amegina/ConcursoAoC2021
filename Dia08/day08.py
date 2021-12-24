def lines():
    with open('./input.txt', 'r') as file:
        return [i.strip() for i in file]


def solve(letters):
    inp = letters[0]
    out = letters[1]
    sol = [""] * 10
    dic = {2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
    for i in inp.split():
        dic[len(i)] += ["".join(sorted(i))]

    sol[1] = dic[2][0]
    sol[7] = dic[3][0]
    sol[4] = dic[4][0]
    sol[8] = dic[7][0]

    sol[3] = [x for x in dic[5] if len(set(sol[1]).intersection(x)) == 2][0]
    dic[5].remove(sol[3])
    sol[5] = [x for x in dic[5] if len(set(sol[4]).intersection(x)) == 3][0]
    dic[5].remove(sol[5])
    sol[2] = dic[5][0]

    sol[6] = [x for x in dic[6] if len(set(sol[1]).intersection(x)) == 1][0]
    dic[6].remove(sol[6])
    sol[9] = [x for x in dic[6] if len(set(sol[4]).intersection(x)) == 4][0]
    dic[6].remove(sol[9])
    sol[0] = dic[6][0]

    return [sol.index("".join(sorted(x))) for x in out.split()]


digits = lines()
easyDigits = 0
total = 0

for line in digits:
    num = solve(line.split(" | "))
    for n in num:
        if n == 1 or n == 4 or n == 7 or n == 8:
            easyDigits += 1
    total += int(''.join(map(str, num)))

print("Star1:", easyDigits)
print("Star1:", total)
