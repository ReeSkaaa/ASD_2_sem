def max_ad_revenue(n, a, b):
    a.sort(reverse=True)  # Сортируем прибыли по убыванию
    b.sort(reverse=True)  # Сортируем количества кликов по убыванию
    max_revenue = 0
    for i in range(n):
        max_revenue += a[i] * b[i]
    return max_revenue

with open("lab_1/tasks/task3/input.txt", "r") as f:
    n = int(f.readline())
    a = list(map(int, f.readline().split()))
    b = list(map(int, f.readline().split()))

result = max_ad_revenue(n, a, b)
with open('lab_1/tasks/task3/output.txt', 'w') as file:
    file.write(str(result))
print(result)