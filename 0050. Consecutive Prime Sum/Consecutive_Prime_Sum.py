
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(limit):
    return [i for i in range(2, limit) if is_prime(i)]

def find_longest_consecutive_prime_sum(limit):
    max_prime = 0
    max_length = 0
    primes = generate_primes(limit)
    for i in range(len(primes)):
        for j in range(i + max_length, len(primes)):
            total_sum = sum(primes[i: j])
            if total_sum > max_prime and total_sum in primes:
                max_prime = total_sum
                max_length = j - i
    return max_prime

limit = 10**6
print(find_longest_consecutive_prime_sum(limit))