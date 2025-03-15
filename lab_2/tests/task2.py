import sys
import time


def find_B(n, h):
    e = 0.005 / (n - 1)
    l = 0  # меньшее из значений, 2 лампа на земле
    r = h[0]
    last = -10 ** 9
    while r > (l + e):
        mid = (l + r) / 2
        prev = h[0]
        cur = mid
        aboveGround = cur > 0
        for i in range(3, n + 1):
            next_height = 2 * cur - prev + 2  # можно получить из заданной формулы
            if next_height <= 0:
                aboveGround = False
            prev = cur
            cur = next_height
        if aboveGround:
            r = mid  # можем понизить
            last = cur
        else:
            l = mid
    return last



n = 8
h = [0] * n  # высоты лампочек
h[0] = 15

# Начало отсчета времени
start_time = time.perf_counter()
answer = str(find_B(n, h))

# Конец отсчета времени
end_time = time.perf_counter()
execution_time = end_time - start_time

total_size = sys.getsizeof(answer)
for item in answer:
    total_size += sys.getsizeof(item)

print(f"Ответ: {answer}")
print(f"Общий размер памти: {total_size} байт")
print(f"Время выполнения: {execution_time:.8f} секунд")
