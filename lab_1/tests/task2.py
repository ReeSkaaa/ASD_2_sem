import sys
import time

def refill_stations(d, m, n, stops):
    stops.append(d)  # Вручную добавляем пункт назначения в список заправок (остановок)
    num_refills = 0
    current_position = 0
    i = 0
    # Если расстояние до пункта назначения меньше или равно максимальному расстоянию,
    # которое можно проехать на одном баке, то заправки не нужны
    if d <= m:
        return 0
    while current_position < d: #Пока мы не на месте назначения, выполняется код в цикле
        last_reachable_stop = -1
        while i < len(stops) and stops[i] <= current_position + m: #Ищем самую далекую от
            #нашего текущего местоположениядостижимую запраку
            last_reachable_stop = i
            i += 1
        if last_reachable_stop == -1: #Если до пункута назначения невозможно 
            #добраться (значение достижимой остановки не обновилось) возвращаем -1
            #и прекращаем дальнейшие вычисления
            return -1
        if stops[last_reachable_stop] != d:  #Пункт назначения заправкой не считается
            num_refills += 1 #Увеличиваем счетчик необхлдимых заправок!
        current_position = stops[last_reachable_stop]

    return num_refills

# Начало отсчета времени
start_time = time.perf_counter()

answer = str(refill_stations(950, 400, 4, [200, 375, 550, 750]))

# Конец отсчета времени
end_time = time.perf_counter()
execution_time = end_time - start_time

total_size = sys.getsizeof(answer)
for item in answer:
    total_size += sys.getsizeof(item)

print(f"Ответ: {answer[0]}")
print(f"Общий размер памти: {total_size} байт")
print(f"Время выполнения: {execution_time:.8f} секунд")