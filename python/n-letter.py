#! /usr/bin/env python2.7
import string, itertools, re, pprint

DICT_LOCATION = '/usr/share/dict/words'

def get_valid_words(wordsize=1):
    'This function returns a list of all valid wordsize-letter words, wordsize>=1'
    if wordsize < 1:
        return None
    with open(DICT_LOCATION) as dictionary:
        return filter(lambda word: len(word) == wordsize, [string.strip(word) for word in dictionary])

if __name__ == '__main__':
    [get_valid_words(i) for i in range(1,50)]
    pprint.pprint(get_valid_words(24))
        
