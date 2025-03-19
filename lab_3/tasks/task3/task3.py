import sys

sys.setrecursionlimit(10000)  # Увеличиваем лимит рекурсии для больших графов


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


with open("input.txt", "r") as f:
    n, m = map(int, f.readline().split())
    edges = [tuple(map(int, f.readline().split())) for i in range(m)]
    has_cycle = find_cycle(n, edges)
    print(edges)
with open("output.txt", "w") as f:
    f.write(str(has_cycle))
