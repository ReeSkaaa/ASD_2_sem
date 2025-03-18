import sys
import time

class Node:
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        def _insert(node, key):
            if not node: return Node(key)
            if key < node.key:
                node.left = _insert(node.left, key)
            elif key > node.key:
                node.right = _insert(node.right, key)
            return node
        self.root = _insert(self.root, key)

    def delete(self, key):
        def _delete(node, key):
            if not node: return None
            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            else:
                if not node.left: return node.right
                if not node.right: return node.left
                min_larger_node = self._min(node.right)
                node.key, node.right = min_larger_node.key, _delete(node.right, min_larger_node.key)
            return node
        self.root = _delete(self.root, key)

    def exists(self, key):
        node = self.root
        while node:
            if key == node.key: return "true"
            node = node.left if key < node.key else node.right
        return "false"

    def next(self, key):
        res, node = None, self.root
        while node:
            if node.key > key:
                res, node = node.key, node.left
            else:
                node = node.right
        return str(res) if res is not None else "none"

    def prev(self, key):
        res, node = None, self.root
        while node:
            if node.key < key:
                res, node = node.key, node.right
            else:
                node = node.left
        return str(res) if res is not None else "none"

    def _min(self, node):
        while node.left:
            node = node.left
        return node

# Начало отсчета времени
start_time = time.perf_counter()

# Создание дерева и выполнение операций
tree = BST()
operations = [
    ("insert", 10),
    ("insert", 20),
    ("insert", 5),
    ("exists", 10),
    ("exists", 15)
]

results = []
for op, value in operations:
    if op == "insert":
        tree.insert(value)
    elif op == "delete":
        tree.delete(value)
    elif op == "exists":
        results.append(tree.exists(value))
    elif op == "next":
        results.append(tree.next(value))
    elif op == "prev":
        results.append(tree.prev(value))

# Конец отсчета времени
end_time = time.perf_counter()
execution_time = end_time - start_time

# Оценка памяти
total_size = sys.getsizeof(tree)
for result in results:
    total_size += sys.getsizeof(result)

# Вывод результатов
print(f"Результаты: {results}")
print(f"Общий размер памяти: {total_size} байт")
print(f"Время выполнения: {execution_time:.8f} секунд")
