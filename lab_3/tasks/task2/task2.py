import sys

sys.setrecursionlimit(10000)  # Увеличиваем лимит рекурсии для больших графов

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


with open("input.txt", "r") as f:
    n, m = map(int, f.readline().split())
    edges = [tuple(map(int, f.readline().split())) for i in range(m)]
    count = find_connected_component(n, edges)
with open("output.txt", "w") as f:
    f.write(str(count))
