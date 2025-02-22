import sys
import time

def LargestNumber(digits):
    answer = ''
    while digits:
        maxDigit = None
        for digit in digits:
            if maxDigit is None:
                maxDigit = digit
            if digit + maxDigit > maxDigit + digit:  # cравниваем конкатенации
                maxDigit = digit
        answer += maxDigit
        digits.remove(maxDigit)
    return answer


# Начало отсчета времени
start_time = time.time()

answer = LargestNumber(['21', '7', '1'])

# Конец отсчета времени
end_time = time.time()
execution_time = end_time - start_time

total_size = sys.getsizeof(answer)
for item in answer:
    total_size += sys.getsizeof(item)

print(f"Ответ: {answer}")
print(f"Общий размер памти: {total_size} байт")
print(f"Время выполнения: {execution_time:.6f} секунд")
