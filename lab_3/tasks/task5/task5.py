import sys
sys.setrecursionlimit(10**6)

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

# Читаем входные данные
with open("lab_3/tasks/task5/input.txt") as file:
    n, m = map(int, file.readline().split())
    edges = [tuple(map(int, line.split())) for line in file]

# Запускаем алгоритм
result = count_scc(n, edges)

# Записываем результат в output.txt
with open("lab_3/tasks/task5/output.txt", "w") as file:
    file.write(str(result))
    print(str(result))
