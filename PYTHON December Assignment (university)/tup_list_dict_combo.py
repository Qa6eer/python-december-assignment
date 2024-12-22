students_scores = {
    "QADEER": (85, 90, 95),
    "TAIF": (80, 85, 88),
    "ABDUL": (78, 82, 84)
}

def average_score(scores):
    return sum(scores) / len(scores)

for name, scores in students_scores.items():
    print(f"{name}: {average_score(scores)}")

highest = max(students_scores.items(), key=lambda x: average_score(x[1]))
print(f"Top student: {highest[0]}")