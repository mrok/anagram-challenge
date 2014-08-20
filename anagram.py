from itertools import *
import hashlib
from datetime import datetime

def trim(p):
    #remove whitespaces
    return p.strip()

#check if letters from word belongs to pattern
def is_word_possible(pattern, word):
    pattern, word = list(pattern), list(word)
    for letter in word:
        if letter in pattern:
            pattern.remove(letter)
        else:
            return False

    return True

confirmation_hash = "4624d200580677270a54ccff86b9610e"
anagram_in = "poultry outwits ants"
anagram_in_list = list(anagram_in)
wordlist = tuple(open('./wordlist', 'r'))
wordlist = map(trim, wordlist)
wordlist = list(set(wordlist)) #remove duplications

possible_words = [item for item in wordlist if is_word_possible(anagram_in, item)]
print 'There are ' + str(len(possible_words)) + ' words to combine'
#so we have only words containing the same letters as initial anagram

print 'Start ' + datetime.now().strftime("%d.%m.%Y %H:%M:%S")
counter = 0
all = float((len(possible_words) ** 3) / 6) # approximately  n!/((n-k)! * k!)
result = []

for combination in combinations(possible_words, 3):
    combination_str = ' '.join(combination)
    if (len(combination_str) == 20): #result has only 20 letter so we can limit amount of calculations
        if (is_word_possible(anagram_in, combination_str)):
            for permutation in permutations(combination, 3):
                if (hashlib.md5(' '.join(permutation)).hexdigest() == confirmation_hash):
                    result.append(' '.join(permutation))

    counter = counter + 1
    if ((counter % 1000000) == 0):
        print "Progress: " + str(round((counter / all) * 100, 4)) + "%"

if len(result) > 0:
    print "Result(s): " + ' --- '.join(result)
else:
    print "No results"