import sys
import time

def count_scc(n, edges):
    from collections import defaultdict

    # Граф и транспонированный граф
    graph = defaultdict(list)
    rev_graph = defaultdict(list)

    # Заполняем граф
    for u, v in edges:
        graph[u].append(v)
        rev_graph[v].append(u)

    visited = set()
    order = []

    def dfs1(v):
        visited.add(v)
        for nei in graph[v]:
            if nei not in visited:
                dfs1(nei)
        order.append(v)

    for v in range(1, n + 1):
        if v not in visited:
            dfs1(v)

    visited.clear()
    scc_count = 0

    def dfs2(v):
        visited.add(v)
        for nei in rev_graph[v]:
            if nei not in visited:
                dfs2(nei)

    while order:
        v = order.pop()
        if v not in visited:
            dfs2(v)
            scc_count += 1 

    return scc_count

# Тестовые данные
test_n = 5
test_edges = [(2, 1), (3, 2), (3, 1), (4, 3), (4, 1), (5, 2), (5, 3)]

# Начало отсчета времени
start_time = time.perf_counter()

answer = count_scc(test_n, test_edges)

# Конец отсчета времени
end_time = time.perf_counter()
execution_time = end_time - start_time

# Оценка потребляемой памяти
total_size = sys.getsizeof(answer)
total_size += sys.getsizeof(test_n)
total_size += sys.getsizeof(test_edges)
for edge in test_edges:
    total_size += sys.getsizeof(edge)
    for node in edge:
        total_size += sys.getsizeof(node)

print(f"Ответ: {answer}")
print(f"Общий размер памяти: {total_size} байт")
print(f"Время выполнения: {execution_time:.8f} секунд")
