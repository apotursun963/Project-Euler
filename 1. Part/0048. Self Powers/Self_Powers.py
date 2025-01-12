
result = 0
limit = 1000
for i in range(1, limit + 1):
    result += i ** i

str_result = str(result)
print(str_result[len(str_result) - 10:])