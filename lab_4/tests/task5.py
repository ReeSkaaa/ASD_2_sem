import sys
import time
def prefix_function(s):
    n = len(s)
    pi = [0] * n  # Инициализация массива префиксной функции
    for i in range(1, n):  # Начинаем с 1, так как pi[0] всегда 0
        j = pi[i - 1]  # Берем значение префиксной функции для предыдущего символа
        while j > 0 and s[i] != s[j]:  # Пока j > 0 и символы не совпадают
            j = pi[j - 1]  # Уменьшаем j
        if s[i] == s[j]:  # Если символы совпали
            j += 1  # Увеличиваем j
        pi[i] = j  # Записываем значение префиксной функции
    return pi

# Начало отсчета времени
start_time = time.perf_counter()

answer = prefix_function('aaaAAA')

# Конец отсчета времени
end_time = time.perf_counter()
execution_time = end_time - start_time

total_size = sys.getsizeof(answer)
for item in answer:
    total_size += sys.getsizeof(item)


print(f"Ответ: {answer}")
print(f"Общий размер памяти: {total_size} байт")
print(f"Время выполнения: {execution_time:.8f} секунд")
