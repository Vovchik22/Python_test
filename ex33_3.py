def NewNumb(first):
    i = 0
    numbers = []
    for i in range(0, 10):
        print(f"Start from {i}")
        numbers.append(i)

        print("Numbers now", numbers)
        print(f"Last number {i}")
    return numbers


numbers = NewNumb(1)

for num in numbers:
    print(num)
