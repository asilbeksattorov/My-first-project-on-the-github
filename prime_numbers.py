# Iterator
"""
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers_iterator():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

prime_iterator = prime_numbers_iterator()

for _ in range(20):
    print(next(prime_iterator))
"""



# Generator
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers_generator():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

prime_generator = prime_numbers_generator()

for _ in range(20):
    print(next(prime_generator))













