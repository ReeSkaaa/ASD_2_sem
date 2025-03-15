def find_B(h, n, e):
    l = 0  # меньшее из значений, 2 лампа на земле
    r = h[0]
    b = -10 ** 9
    while r > (l + e):
        mid = (l + r) / 2
        prev = h[0]
        cur = mid
        aboveGround = cur > 0
        for i in range(3, n + 1):
            next_height = 2 * cur - prev + 2  # можно получить из заданной формулы
            if next_height < 0:
                aboveGround = False
            prev = cur
            cur = next_height
        if aboveGround:
            r = mid  # можем понизить
            last = cur
        else:
            l = mid
    return last


with open('lab_2/tasks/task2/input.txt', 'r') as file:
    n, A = map(float, file.readline().split())
    n = int(n)
    h = [0] * n  # высоты лампочек
    h[0] = A
    e = 0.005 / (n - 1)
    B = str(find_B(h, n, e))
with open('lab_2/tasks/task2/output.txt', 'w') as file:
    file.write(B)
print(B)
