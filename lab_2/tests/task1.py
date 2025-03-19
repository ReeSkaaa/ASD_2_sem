import sys
import time

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def build_tree(node_data):

    nodes = [Node(data[0]) for data in node_data]
    root = None

    for i, data in enumerate(node_data):
        left_index = data[1]
        right_index = data[2]

        if left_index != -1:
            nodes[i].left = nodes[left_index]
        if right_index != -1:
            nodes[i].right = nodes[right_index]

        # Узел 0 - корень
        if i == 0:
            root = nodes[0]

    return nodes

def inorder_traversal(node):
    result = []
    if node:
        result += inorder_traversal(node.left)
        result.append(str(node.key))
        result += inorder_traversal(node.right)
    return result

def preorder_traversal(node):
    result = []
    if node:
        result.append(str(node.key))
        result += preorder_traversal(node.left)
        result += preorder_traversal(node.right)
    return result

def postorder_traversal(node):
    result = []
    if node:
        result += postorder_traversal(node.left)
        result += postorder_traversal(node.right)
        result.append(str(node.key))
    return result
#Cборка дерева в измерении суммарной скорости работы 3 лгоритмов прохода не участвует
node_data = [(4, 1, 2), (2, 3, 4), (5, -1, -1), (1, -1, -1), (3, -1, -1)]
nodes = build_tree(node_data)
root = nodes[0]

# Начало отсчета времени
start_time = time.perf_counter()

inorder = inorder_traversal(root)
preorder = preorder_traversal(root)
postorder = postorder_traversal(root)
answer = str("\n" + " ".join(inorder) + "\n" + " ".join(preorder) + "\n" + " ".join(postorder))

# Конец отсчета времени
end_time = time.perf_counter()
execution_time = end_time - start_time

total_size = sys.getsizeof(answer)
for item in answer:
    total_size += sys.getsizeof(item)

print(f"Ответ: {answer}")
print(f"Общий размер памти: {total_size} байт")
print(f"Время выполнения: {execution_time:.8f} секунд")