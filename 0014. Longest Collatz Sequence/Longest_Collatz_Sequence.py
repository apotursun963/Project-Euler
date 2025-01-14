
def calculate_collatz(num):
    counter = 1
    while num != 1:
        if num % 2 == 0:
            num //= 2
            counter += 1
        elif num % 2 == 1:
            num = (num * 3) + 1
            counter += 1
    return (counter)

max_chain_len = 0
max_chain_num = 0
for i in range(1, 1000000):
    lenght = calculate_collatz(i)
    if lenght > max_chain_len:
        max_chain_len = lenght
        max_chain_num = i

print(f"number: {max_chain_num} chain len: {max_chain_len}")
