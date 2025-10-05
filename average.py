
def calculate_average(numbers):
    breakpoint()
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

# Test it
scores = [85, 90, 78, 92, 88]
avg = calculate_average(scores)
print(f"Average score: {avg}")

# This should work too
empty_scores = []
avg2 = calculate_average(empty_scores)
print(f"Average of empty list: {avg2}")