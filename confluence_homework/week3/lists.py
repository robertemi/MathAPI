numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[-1])
print(numbers[len(numbers) // 2])

numbers.append(60)
numbers.insert(1, 15)
numbers.pop()
print(len(numbers) + 1)
print(numbers.sort())