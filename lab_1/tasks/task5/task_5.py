def find_max_prizes(n):
    prizes = []
    i = 1  # текущее кол-во конфет
    k = 0  # количество призов
    # Используем цикл для распределения конфет
    while n >= i:
        prizes.append(i)  # добавляем кол-во конфет
        n -= i  # уменьшение кол-ва конфет
        i += 1  # кол-во конфет для следующего места
        k += 1
        # если остались незадействованные конфеты
    if n > 0:
        prizes[-1] += n
    return k, prizes


with open('input.txt', 'r') as file:
    n = int(file.read())
    k, prizes = find_max_prizes(n)
with open('output.txt', 'w') as file:
    file.write(f"{k}\n")
    file.write(f" ".join(map(str, prizes)))
