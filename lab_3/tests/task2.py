import sys
import time

def find_connected_component(n, edges):
    # Создание списка смежности
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # Массив для отметки посещенных вершин
    visited = [False] * (n + 1)

    # Функция DFS для обхода компоненты связности
    def dfs(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs(v)

    # Подсчет компонент связности
    count = 0
    for u in range(1, n + 1):
        if not visited[u]:
            dfs(u)
            count += 1
    return count

# Тестовые данные
test_n = 5
test_edges = [(1, 2), (2, 3), (3, 1), (3, 4), (4, 5)]

# Начало отсчета времени
start_time = time.perf_counter()

edges = [(1, 2), (3, 2)]
answer = find_connected_component(4, edges)

# Конец отсчета времени
end_time = time.perf_counter()
execution_time = end_time - start_time

total_size = sys.getsizeof(answer)

print(f"Ответ: {answer}")
print(f"Общий размер памяти: {total_size} байт")
print(f"Время выполнения: {execution_time:.8f} секунд")
