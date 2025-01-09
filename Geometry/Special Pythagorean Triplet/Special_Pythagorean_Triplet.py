
def find_pythagorean_triple():
    a = 1
    while a < 1000:
        b = a + 1
        while b < 1000 - a:
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                return a, b, c
            b += 1
        a += 1

while True:
    x, y, z = find_pythagorean_triple()
    if x + y + z == 1000:
        print(x * y * z)
        break
