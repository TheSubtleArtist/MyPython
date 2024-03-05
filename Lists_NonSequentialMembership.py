odds = list(range(1, 20, 2))
print(odds, end=" ")

evens = list(range(0, 100, 2))
print(evens, end=" ")
print()
odds = list(range(1, 99, 2))
print(odds, end=" ")

print(list(range(0, 31, 3)), end=" ")

squares = []
for value in range(1, 11):
	square = value ** 2
	squares.append(square)
print(squares)

squares = []
for value in range(1, 11):
	squares.append(value ** 2)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))

# List comprehensions

squares = [value ** 2 for value in range(1, 11)]
print(squares)