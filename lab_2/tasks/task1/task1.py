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

# Чтение входного файла
with open("lab_2/tasks/task1/input.txt") as f:
    n = int(f.readline().strip())
    node_data = []
    for _ in range(n):
        key, left_index, right_index = map(int, f.readline().strip().split())
        node_data.append((key, left_index, right_index))

# Построение дерева
    nodes = build_tree(node_data)
    root = nodes[0]

    # Выполнение обходов дерева
    inorder = inorder_traversal(root)
    preorder = preorder_traversal(root)
    postorder = postorder_traversal(root)

# Запись выходного файла
with open("lab_2/tasks/task1/output.txt", "w") as f:
    f.write(" ".join(inorder) + "\n")
    f.write(" ".join(preorder)+ "\n")
    f.write(" ".join(postorder)+ "\n")
print(" ".join(inorder))
print(" ".join(preorder))
print(" ".join(postorder))