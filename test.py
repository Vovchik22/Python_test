def longest_consec(strarr, k):
    n = len(strarr)
    if n == 0 or k > n or k <= 0:
        return ''

    longest = index = 0
    '''for i in range(n - k + 1):
        print(i)'''
        length = sum([len(s) for s in strarr[i: i + k]])
        print(length)
        '''if length > longest:
            longest = length
            index = i'''

    '''return ''.join(strarr[index: index + k])'''


print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
print(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2))
