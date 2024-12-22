import random

def generate_random_numbers(n, a, b):
    return [random.randint(a, b) for _ in range(n)]

print(generate_random_numbers(5, 1, 10))