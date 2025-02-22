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


with open('input.txt', 'r') as file:
    n = int(file.readline().strip())
    digits = list(map(str, file.readline().split()))
result = LargestNumber(digits)
with open('output.txt', 'w') as file:
    file.write(result)
