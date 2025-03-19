def rope_operation(s, queries):
    """
    Выполняет операции веревки (rope) над строкой s.

    Args:
        s: Исходная строка.
        queries: Список запросов, каждый запрос - это кортеж (i, j, k).

    Returns:
        Строка после выполнения всех запросов.
    """

    for i, j, k in queries:
        # 1. Вырезаем подстроку s[i:j+1]
        substring = s[i:j+1]
        s = s[:i] + s[j+1:]

        # 2. Вставляем вырезанную подстроку после k-го символа
        s = s[:k] + substring + s[k:]

    return s


# Чтение входного файла
with open("lab_2/tasks/task18/input.txt") as file:
    s = file.readline().strip()
    n = int(file.readline().strip())
    queries = []
    for _ in range(n):
        i, j, k = map(int, file.readline().strip().split())
        queries.append((i, j, k))

 # Выполнение операций веревки
result = rope_operation(s, queries)


# Запись выходного файла
with open("lab_2/tasks/task18/output.txt", "w") as file:
    file.write(result)
