numbers = [12,53,110,14,79]

largest = numbers[0]
for i in numbers:
    if i > largest:
        largest = i

print(numbers)
print(f'Largest: {largest}')
