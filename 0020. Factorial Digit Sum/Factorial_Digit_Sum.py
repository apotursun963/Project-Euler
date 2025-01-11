
def factorial(num):
    result = 1
    while num > 0:
        result *= num
        num -= 1
    return result

digit_sum = 0
number = factorial(100)
for i in str(number):
    digit_sum += int(i)

print(digit_sum)
