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
            return #если операция выполнилась, заканчиваем
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
                return  # элемент уже существует

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


bst = BST() #создаем дерево
with open('lab_2/tasks/task3/input.txt', 'r') as infile, open('lab_2/tasks/task3/output.txt', 'w') as outfile:
    for line in infile:
        parts = line.strip().split()
        command = parts[0]
        x = int(parts[1])
        if command == '+':
            bst.insert(x)
        elif command == '>':
            result = bst.find_min_greater(x)
            outfile.write(str(result) + '\n')
print(str(result))

