"""# palindrome number
n = 0

for a in range (100, int(999 + 1), 1):
    for b in range (a, int(999 + 1), 1):
        x = a * b
        if x > n:
            s  = str(a * b)
            if s == s [:: -1]:
                n = a * b

print(n)

l = ['assa', 'test', 'caca']

def palindrome (l):
    for i in range(int(len(l) // 2)):
        if l[i] != l[-1 - i]:
            return False
    return True

for i in l:
    print (palindrome(i))
"""

def is_palindrome (n):
    return str(n) == str(n)[::-1]

if __name__ == "__main__":
    print ('{} and {} => {}'.format(*max((i, j, i*j)
                for i in range (1000, 900, -1)
                        for j in range (1000, 900,  -1)
                            if is_palindrome(i*j))))
