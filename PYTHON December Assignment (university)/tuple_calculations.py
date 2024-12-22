numbers = (1, 2, 3, 4, 5)
print(sum(numbers))  # Output: 15
print(max(numbers))  # Output: 5
print(min(numbers))  # Output: 1

random_numbers = tuple(random.randint(1, 10) for _ in range(5))
print(random_numbers)
if 7 in random_numbers:
    print("7 is in the tuple.")
else:
    print("7 is not in the tuple.")