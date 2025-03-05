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

with open("lab_1/tasks/task7/input.txt", "r") as f:
    K, n = map(int, f.readline().split())
    t = list(map(int, f.readline().split()))

result = str(max_boots_repaired(K, n, t))
with open('lab_1/tasks/task7/output.txt', 'w') as file:
    file.write(result)
print(result)