
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_pandigital_num(num):
    digits = set()
    for i in range(1, len(str(num)) + 1):
        digits.add(str(i))
    if set(str(num)) == digits:
        return True

for number in range(7654321, 1, -1):
    if is_prime(number) and is_pandigital_num(number):
        print(number)
        break
