import sys
import time
import random

def max_ad_revenue(n, a, b):
    a.sort(reverse=True)  # Сортируем прибыли по убыванию
    b.sort(reverse=True)  # Сортируем количества кликов по убыванию
    max_revenue = 0
    for i in range(n):
        max_revenue += a[i] * b[i]
    return max_revenue

# Начало отсчета времени
start_time = time.perf_counter()
answer = str(max_ad_revenue(1, [23], [39]))

# Конец отсчета времени
end_time = time.perf_counter()
execution_time = end_time - start_time

total_size = sys.getsizeof(answer)
for item in answer:
    total_size += sys.getsizeof(item)

print(f"Ответ: {answer}")
print(f"Общий размер памти: {total_size} байт")
print(f"Время выполнения: {execution_time:.8f} секунд")