def break_word (stuff):
    '''This function will break some words for us'''
    words = stuff.split()
    return words

def sort_words (words):
    '''sort words'''
    return sorted (words)

def print_first (words):
    '''print the first word after popping it off'''
    word = words.pop(0)
    print(word)

def print_last (words):
    ''' Printing last word after poppin'''
    word = words.pop(-1)
    print(word)

def sort_sentence (sentence):
    '''takes in a full sentence and returns the sorted words'''
    words = break_word(sentence)
    return  sort_words(words)

def print_the_last_and_first (sentence):
    ''' print the first and the last words of the sentence'''
    words = break_word (sentence)
    print_first(words)
    print_last(words)

def print_the_first_and_last_sorted (sentence):
    '''sorts the words then prints the first and the last'''
    words = sort_sentence(sentence)
    print_first(words)
    print_last(words)

sentence = "All good things come to those who wait."
