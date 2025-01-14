
sum_of_digits = 0
number = 2**1000

while number > 0:
    sum_of_digits += number % 10
    number //= 10
print(sum_of_digits)
