
sum_of_squares = 0
sum_of_numbers = 0

for i in range(1, 101):
    sum_of_squares += i * i
    sum_of_numbers += i

gap = sum_of_numbers**2 - sum_of_squares
print(gap)
