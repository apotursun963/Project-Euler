
import math

def is_curious_number(number):
    total = 0
    save = number
    while number != 0:
        total += math.factorial(number % 10)
        number //= 10
    return total == save

res = 0
limit = 1000000
for i in range(10, limit):
    if is_curious_number(i):
        res += i
print(res)
