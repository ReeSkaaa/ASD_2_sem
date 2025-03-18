import sys
import time

def compute_z_function(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z

# Тестовые данные
test_string = "abacaba"

# Начало отсчета времени
start_time = time.perf_counter()

answer = compute_z_function(test_string)

# Конец отсчета времени
end_time = time.perf_counter()
execution_time = end_time - start_time

# Оценка потребляемой памяти
total_size = sys.getsizeof(answer)
total_size += sys.getsizeof(test_string)
for value in answer:
    total_size += sys.getsizeof(value)

print(f"Ответ: {answer[1:]}")
print(f"Общий размер памяти: {total_size} байт")
print(f"Время выполнения: {execution_time:.8f} секунд")


