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


# Чтение входного файла
with open("input.txt") as file:
    lines = file.read().splitlines()

tree, output = BST(), []

for line in lines:
    cmd, x = line.split()
    x = int(x)
    if cmd == "insert":
        tree.insert(x)
    elif cmd == "delete":
        tree.delete(x)
    elif cmd == "exists":
        output.append(tree.exists(x))
    elif cmd == "next":
        output.append(tree.next(x))
    elif cmd == "prev":
        output.append(tree.prev(x))

# Запись выходного файла
with open("output.txt", "w") as file:
    file.write("\n".join(output))
