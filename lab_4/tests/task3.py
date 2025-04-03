import sys
import time

def text_patterns(pattern, text):
    occurrences = []
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            occurrences.append(i + 1)  # Номера позиций начинаются с 1
    return occurrences

start_time = time.perf_counter()

answer = text_patterns('aaaaa', "baaaaaaa")
entr_num = [len(answer)]

# Конец отсчета времени
end_time = time.perf_counter()
execution_time = end_time - start_time

total_size = sys.getsizeof(answer) + sys.getsizeof(entr_num)

print(f"Ответ: {entr_num, answer}")
print(f"Общий размер памяти: {total_size} байт")
print(f"Время выполнения: {execution_time:.8f} секунд")