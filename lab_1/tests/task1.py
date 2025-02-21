import sys
import time


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


# Начало отсчета времени
start_time = time.time()

answer = Knapsack(10, [30.0], [500.0], 1)

# Конец отсчета времени
end_time = time.time()
execution_time = end_time - start_time

total_size = sys.getsizeof(answer)
for item in answer:
    total_size += sys.getsizeof(item)

print(f"Ответ: {answer[0]}")
print(f"Общий размер памти: {total_size} байт")
print(f"Время выполнения: {execution_time:.6f} секунд")
