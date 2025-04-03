def prefix_function(s):
    n = len(s)
    pi = [0] * n  # Инициализация массива префиксной функции
    for i in range(1, n):  # Начинаем с 1, так как pi[0] всегда 0
        j = pi[i - 1]  # Берем значение префиксной функции для предыдущего символа
        while j > 0 and s[i] != s[j]:  # Пока j > 0 и символы не совпадают
            j = pi[j - 1]  # Уменьшаем j
        if s[i] == s[j]:  # Если символы совпали
            j += 1  # Увеличиваем j
        pi[i] = j  # Записываем значение префиксной функции
    return pi

with open("lab_4/tasks/task5/input.txt", "r") as f:
    s = f.readline().strip()
    result = prefix_function(s)
with open("lab_4/tasks/task5/output.txt", "w") as f:
    f.write(" ".join(map(str, result)))
    print(" ".join(map(str, result)))
