# import nath module to use a SQR root to find factors from big number
import math

# get factors of a number
def primefactors(number):  # construct a function to determine and calculate factors
    factors = [] # list of factors
    for potentialFactor in range(1, int(math.sqrt(number)) + 1): # for factors in range from 1 to sqr root of inputed number
        if number % potentialFactor == 0: # define that a factor is not have any mod from number
            factors.append(potentialFactor) # add to list factors
            factors.append(number // potentialFactor) # add to list factors themselves 17 % 1 = 0  and 17 // 1 = 17, so we include for calculations and last number
    return factors # get factors

number = int(input('>> Enter a number: '))
print(primefactors(number))

# determing prime number
def prime (number):
    return len(primefactors(number)) == 2

print(f'For {number} is prime %s' % prime(number))


# find highest number

large_prime = 0
for factor in primefactors(number):
    if prime (factor) and factor > large_prime:
        large_prime = factor

print (f'for {number} the largest prime factor is %d' % large_prime)
