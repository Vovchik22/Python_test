i = 10
numbers  =[11, 12, 16]

while i < 20:
    print(f"At he top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bootom i is {i}")

print("The numbers:  ")

for num in numbers:
    print(num)
