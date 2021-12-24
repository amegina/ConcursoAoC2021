def numbers():
    with open('./input.txt', 'r') as file:
        return [int(i.strip()) for i in file]


def decrease(n):
    dec = 0
    for i, n in enumerate(nums[n:]):
        if n > nums[i]:
            dec += 1
    return dec


nums = numbers()

print("Star1:", decrease(1))
print("Star2:", decrease(3))
