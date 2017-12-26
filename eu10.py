'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
L = 20

f = [i for i in range(0, int(L + 1))]

for x in f[2:]:
    if f[x] != 0:
       n = 2
       print ("excluding all  numbers // {}".format(x))
       while x*n < L:
            f[x*n] = 0
            n+=1

print(sum([i for i in f if i !=0]))
