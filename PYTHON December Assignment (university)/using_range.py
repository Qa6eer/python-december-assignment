def sum_of_evens(n):
    return sum(i for i in range(n + 1) if i % 2 == 0)

print(sum_of_evens(10)) 