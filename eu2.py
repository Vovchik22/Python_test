
a = 0
b = 1
fibo = 0

while b <= 4000000:
    if b % 2 == 0:
        fibo += b
    a,b = b, a + b
print(fibo)


# generate fibonacci nubers
# set variables

max_number = int(input('limit a number of fibonaccci sequence \n'))

fibo = [1, 2]
while fibo[-1] < max_number:
    fibo.append(fibo[-1] + fibo[-2])

del fibo[-1]

print (fibo)

# find all the even numbers
even_numbers = []
for numbers in fibo:
    if numbers % 2 == 0:
        even_numbers.append(numbers)

print('*' * 50,"\n",'even numbers are: \n', even_numbers)

# sum of the even numbers foundede
sum_num = 0
for num in even_numbers:
    sum_num += num

print ('sum of even numers is: ', sum_num)
