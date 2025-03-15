import sys
import time

from lab_2.tasks.task3.task3 import result


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    return
                current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = Node(value)
                    return
                current = current.right
            else:
                return  # Элемент уже существует

    def find_min_greater(self, value):
        result = 0
        current = self.root
        while current is not None:
            if current.value > value:
                result = current.value
                current = current.left
            else:
                current = current.right
        return result


bst = BST()  # создаем дерево
answer = []
# Начало отсчета времени
start_time = time.perf_counter()
infile = ['+ 1', '+ 3', '+ 3', '> 1', '> 2', '> 3', '+ 2', '> 1']
for line in infile:
    parts = line.split()
    command = parts[0]
    x = int(parts[1])
    if command == '+':
        bst.insert(x)
    elif command == '>':
        answer.append(bst.find_min_greater(x))

# Конец отсчета времени
end_time = time.perf_counter()
execution_time = end_time - start_time

total_size = sys.getsizeof(answer)
for item in answer:
    total_size += sys.getsizeof(item)

print(f"Ответ: {answer}")
print(f"Общий размер памти: {total_size} байт")
print(f"Время выполнения: {execution_time:.8f} секунд")
