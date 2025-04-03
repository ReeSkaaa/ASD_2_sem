import sys
import time

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

# Начало отсчета времени
start_time = time.perf_counter()
answer = solve_maze(1, 4, {1: [2], 2: [1, 3], 3: [2], 4: []})

# Конец отсчета времени
end_time = time.perf_counter()
execution_time = end_time - start_time

total_size = sys.getsizeof(answer)

print(f"Ответ: {answer}")
print(f"Общий размер памяти: {total_size} байт")
print(f"Время выполнения: {execution_time:.8f} секунд")