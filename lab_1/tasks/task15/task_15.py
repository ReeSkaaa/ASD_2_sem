import time
import tracemalloc


def make_valid_brackets(s):
    stack = []
    indices_to_keep = set()

    # Соответствия закрывающих скобок их открывающим
    bracket_pairs = {')': '(', ']': '[', '}': '{'}
    open_brackets = set(bracket_pairs.values())

    # Первый проход: находим корректные пары скобок
    for i, char in enumerate(s):
        if char in open_brackets:
            stack.append((char, i))
        elif char in bracket_pairs:
            if stack and stack[-1][0] == bracket_pairs[char]:
                indices_to_keep.add(i)
                indices_to_keep.add(stack[-1][1])
                stack.pop()

    # Второй проход: собираем итоговую строку
    result = ''.join(s[i] for i in sorted(indices_to_keep))
    return result


with open('lab_1/tasks/task15/input.txt', 'r') as file:
    s = file.readline().strip()
valid_brackets = make_valid_brackets(s)
with open('lab_1/tasks/task15/output.txt', 'w') as file:
    file.write(valid_brackets)
    print(valid_brackets)