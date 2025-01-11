
import math

def is_prime(num):
    if num <= 1:
        return 0
    for i in range(2, int(math.sqrt(num)) + 1):
        if (num % i == 0):
            return 0
    return 1

prime = 0
counter = 0
while True:
    prime += 1
    if (is_prime(prime)):
        counter += 1
        if (counter == 10001):
            print(prime)
            break
