def compute_z_function(s):
    n = len(s)
    z = [0] * n
    l, r, = 0, 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z

# Чтение входных данных
with open("lab_4/tasks/task6/input.txt", "r") as file:
    s = file.readline().strip()

# Вычисление Z-функции
z_values = compute_z_function(s)

# Запись выходных данных
with open("lab_4/tasks/task6/output.txt", "w") as file:
    file.write(" ".join(map(str, z_values[1:])))
    print(" ".join(map(str, z_values[1:])))
