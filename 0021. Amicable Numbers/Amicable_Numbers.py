
def is_amicable_numbers(num1, num2):
    num1_divisors = 0
    num2_divisors = 0
    for i in range(1, num1):
        if num1 % i == 0:
            num1_divisors += i
    for j in range(1, num2):
        if num2 % j == 0:
            num2_divisors += j
    return num1_divisors == num2 and num2_divisors == num1

total = 0
limit = 10000
for i in range(1, limit):
    pair = sum(j for j in range(1, i) if i % j == 0)
    if pair > i and is_amicable_numbers(i, pair):
        total += i + pair

print(total)