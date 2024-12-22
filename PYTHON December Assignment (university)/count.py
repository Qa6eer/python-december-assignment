def count_characters(string):
    count = {}
    for char in string:
        count[char] = count.get(char, 0) + 1
    return count

print(count_characters("QADEER"))