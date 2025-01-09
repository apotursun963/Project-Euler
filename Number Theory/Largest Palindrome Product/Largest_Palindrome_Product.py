
def is_palindorme(number):
    num_str = str(number)
    return num_str == num_str[::-1]

max_palindrome = 0
for i in range(10, 1000):
    for j in range(i , 1000):
        product = i * j
        if is_palindorme(product) and product > max_palindrome:
            max_palindrome = product

print(max_palindrome)
