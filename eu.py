# loop over numbers from  1 to 1000
numbers = []
for n in range (1, 1000):
    if n % 3 == 0 or n % 5 == 0:
        numbers.append(n)
print(numbers)

print(sum(numbers))
