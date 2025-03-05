def refill_stations(d, m, n, stops):
    stops.append(d)  # Вручную добавляем пункт назначения в список заправок (остановок)
    num_refills = 0
    current_position = 0
    i = 0
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

with open("lab_1/tasks/task2/input.txt", "r") as f:
    d = int(f.readline()) #Расстояние до пункта назначения в км
    m = int(f.readline()) #Расстояние, которое автомобиль проедет на полном баке
    n = int(f.readline()) #Общее количество заправок на пути
    stops = list(map(int, f.readline().split())) #Список расстояний от страртовой 
    # точки до каждой из n заправок
answer = str(refill_stations(d, m, n, stops))   
with open('lab_1/tasks/task2/output.txt', 'w') as file:
    file.write(answer)
print(answer)
