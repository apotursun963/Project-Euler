
import math

def is_prime(num):
    if num <= 1:
        return 0
    for i in range(2, int(math.sqrt(num)) + 1):
        if (num % i == 0):
            return 0
    return 1

print(sum(i for i in range(2000000) if (is_prime(i))))
