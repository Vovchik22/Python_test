import random
from urllib.request import urlopen
import sys

word_url = "http://learncodethehardway.org/words.txt"

phrases = {
'class %%%(%%%):':
'Make a class named %%% taht is-a %%%.',
'class %%% (object):\n\tdef __init__(self, ***)':
'class %%% has-a __init__ that takes self and *** parameteres',
'class %%%(object):\n\tdef ***(self, @@@)':
'class %%% has-a function *** that takes self and @@@',
'"*** = %%%()':
'Set *** to an instance of class %%%.',
'***.***(@@@)':
'From *** get the *** function, call it with params',
'***.*** = "***":':
'From *** get the *** attribute and set it to "***".'
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == 'english':
    phrase_first = True
else:
    phrase_first = False

# load in the words from the website
for word in urlopen(word_url).readlines():
    words.append(str(word.strip(), encoding = 'utf-8'))
