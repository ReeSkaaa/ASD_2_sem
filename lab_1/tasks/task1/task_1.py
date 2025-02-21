def Knapsack(W, w, p, n):
    A = [0] * n  # массив взятых предметов
    V = 0  # общая стоимость содержимого рюкзака
    for i in range(n):
        if W == 0:  # если у нас рюкзак с нулевой вместимостью или место закончилось
            return V, A
        a = min(w[i], W)
        V = V + a * (p[i] / w[i])  # добавляем стоимость предмета
        w[i] = w[i] - a  # уменьшаем оставшийся вес предмета
        A[i] = A[i] + a  # увеличиваем количество взятых предметов
        W = W - a  # уменьшаем оставшуюся вместимость рюкзака
    return V, A


with open('input.txt', 'r') as file:
    data = [line.strip() for line in file.readlines()]
    n, W = map(int, data[0].split())
    p, w = [], []
    for i in range(1, n + 1):
        price, weight = map(float, data[i].split())
        p.append(price)
        w.append(weight)

items = [(p[i] / w[i], p[i], w[i], i) for i in range(n)]  # (удельная стоимость, цена, вес, индекс)
items.sort(reverse=True, key=lambda x: x[0])  # сортируем по убыванию удельной стоимости

# отсортированные массивы цены и веса
sorted_p = [item[1] for item in items]
sorted_w = [item[2] for item in items]
answer = Knapsack(W, sorted_w, sorted_p, n)
formatted_answer = f"{answer[0]:.5f}"  # после запятой должно указываться минимум 4 символа
with open('output.txt', 'w') as file:
    print(formatted_answer, file=file)
print(formatted_answer)
