import sys
import time


def find_max_prizes(n):
    prizes = []
    i = 1  # текущее кол-во конфет на i-ом месте
    k = 0  # количество призов
    # Используем цикл для распределения конфет
    while n >= i:
        prizes.append(i)  # добавляем кол-во конфет, соотв. месту i
        n -= i  # уменьшение кол-ва конфет на i
        i += 1  # кол-во конфет для следующего места
        k += 1
        # если остались незадействованные  конфеты
    if n > 0:
        prizes[-1] += n
    return k, prizes


# Начало отсчета времени
start_time = time.time()

answer = find_max_prizes(6)

# Конец отсчета времени
end_time = time.time()
execution_time = end_time - start_time

total_size = sys.getsizeof(answer)
for item in answer:
    total_size += sys.getsizeof(item)

print(f"Ответ: {answer[0]}")
print(f"Общий размер памти: {total_size} байт")
print(f"Время выполнения: {execution_time:.6f} секунд")
