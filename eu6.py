sqrssum = 0
for i in range (1, 101):
    sqrssum += i * i

sumsqrs = 0
for i in range (1, 101):
    sumsqrs += i
sumsqrs = sumsqrs * sumsqrs

print (sqrssum - sumsqrs)
