# http://exercism.io/exercises/python/isogram/readme
# https://www.youtube.com/watch?v=mbRf7wbMjVs&index=4&list=PL0-84-yl1fUkK3PV8RHT0XskLhxPVE_Y1
def is_isogram(word):
    letters = set()

    word = word.lower()

    for character in word:
        if not character.isalpha():
            continue
        if character in letters:
            return False
                
        letters.add(character)
    return True
