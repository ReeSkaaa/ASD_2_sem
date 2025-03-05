import sys
import time

def max_boots_repaired(K, n, t):
   
    t.sort()  # Сортируем время починки сапог по возрастанию
    boots_repaired = 0
    time_used = 0
    for i in range(n):
        if time_used + t[i] <= K: # Пока рабочий день не закончен,
            #обновляем время и увеличиваем счетчик починеных пар обуви
            time_used += t[i]
            boots_repaired += 1
        else:
            break # Когда рабочий чел закончен, прекращаем вычисления
    return boots_repaired

# Начало отсчета времени
start_time = time.perf_counter()

answer = str(max_boots_repaired(10, 3, [6, 2, 8]))

# Конец отсчета времени
end_time = time.perf_counter()
execution_time = end_time - start_time

total_size = sys.getsizeof(answer)
for item in answer:
    total_size += sys.getsizeof(item)

print(f"Ответ: {answer[0]}")
print(f"Общий размер памти: {total_size} байт")
print(f"Время выполнения: {execution_time:.8f} секунд")