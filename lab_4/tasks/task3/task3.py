def text_patterns(pattern, text):
    occurrences = []
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            occurrences.append(i + 1)  # Номера позиций начинаются с 1
    return occurrences

with open("lab_4/tasks/task3/input.txt", "r") as f:
    pattern = f.readline().strip()
    text = f.readline().strip()
    occurrences = text_patterns(pattern, text)

with open("lab_4/tasks/task3/output.txt", "w") as f:
    f.write(str(len(occurrences)) + "\n")
    print(str(len(occurrences)))
    f.write(" ".join(map(str, occurrences)))  
    print(" ".join(map(str, occurrences)))     
