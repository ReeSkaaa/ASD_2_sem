import sys
import time

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

# Начало отсчета времени
start_time = time.time()

answer = make_valid_brackets("([)]")

# Конец отсчета времени
end_time = time.time()
execution_time = end_time - start_time

total_size = sys.getsizeof(answer)
for item in answer:
    total_size += sys.getsizeof(item)

print(f"Ответ: {answer}")
print(f"Общий размер памти: {total_size} байт")
print(f"Время выполнения: {execution_time:.6f} секунд")