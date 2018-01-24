def factor_function (number):
    factors = []
    for factor in range (1, number + 1):
        if number % factor ==  0:
            factors.append(factor)
            factors.append(number // factor)
    return factors

number = 101
print(factor_function(number))

def prime (number):
    return len(factor_function(number)) == 2

print (prime(number))

largest = 0
for factor in factor_function(number):
    if prime (factor) and factor > largest:
        largest = factor

print(largest)
