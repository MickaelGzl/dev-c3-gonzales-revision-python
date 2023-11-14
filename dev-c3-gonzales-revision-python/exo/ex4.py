import math
import random


numbers = []
for i in range(10):
    numbers.append(math.floor(random.random() * 100))

print(numbers)

total = numbers[0]
max = numbers[0]
min = numbers[0]

for i in range(1, len(numbers)):
    total = total + numbers[i]
    moy = total / (i+1)
    if numbers[i] < min:
        min = numbers[i]
    elif numbers[i] > max:
        max = numbers[i]
    print(f"opération {i}: moyenne: {moy}, maximum: {max}, min: {min}")


