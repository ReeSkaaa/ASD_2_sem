def solve_maze(start_node, end_node, graph):
    visited = set()
    queue = [start_node]
    visited.add(start_node)

    while queue:
        node = queue.pop(0)
        if node == end_node:
            return 1

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return 0

with open("lab_3/tasks/task1/input.txt", "r") as f:
    n, m = map(int, f.readline().split())
    graph = {i: [] for i in range(1, n + 1)}
    for _ in range(m):
        u, v = map(int, f.readline().split())
        graph[u].append(v)
        graph[v].append(u) 
        
    start_node, end_node = map(int, f.readline().split())
    result = str(solve_maze(start_node, end_node, graph))

with open("lab_3/tasks/task1/output.txt", "w") as f:
    f.write(result)
    print(result)