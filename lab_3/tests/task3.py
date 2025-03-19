import sys
import time

def find_cycle(n, edges):
    # Создание списка смежности
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)

    # Массивы для отметки посещенных вершин и текущего пути
    visited = [False] * (n + 1)
    in_path = [False] * (n + 1)

    # Функция DFS для поиска циклов
    def dfs(u):
        if in_path[u]:
            return True  # Найден цикл
        if visited[u]:
            return False  # Вершина уже обработана

        visited[u] = True
        in_path[u] = True

        for v in adj[u]:
            if dfs(v):
                return True

        in_path[u] = False
        return False

    # Проверка наличия циклов
    has_cycle = 0
    for u in range(1, n + 1):
        if not visited[u]:
            if dfs(u):
                has_cycle = 1
                break
    return has_cycle

# Тестовые данные
test_n = 5
test_edges = [(1, 2), (2, 3), (3, 1), (3, 4), (4, 5)]

# Начало отсчета времени
start_time = time.perf_counter()

edges = [(1, 2), (2, 3), (1, 3), (3, 4), (1, 4), (2, 5), (3, 5)]
answer = find_cycle(5, edges)

# Конец отсчета времени
end_time = time.perf_counter()
execution_time = end_time - start_time

total_size = sys.getsizeof(answer)

print(f"Ответ: {answer}")
print(f"Общий размер памяти: {total_size} байт")
print(f"Время выполнения: {execution_time:.8f} секунд")
