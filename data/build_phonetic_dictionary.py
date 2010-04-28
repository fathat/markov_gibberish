#!/usr/bin/env python
"""Note: This requires PyHyphen!

http://pypi.python.org/pypi/PyHyphen/

"""
from hyphen import hyphenator

def pair_with_next(syls):
    return zip(syls, syls[1:])

def read_text_dictionary(dictionary_filename):
    lines = open(dictionary_filename).readlines()
    return [x.strip() for x in lines]

def build_phonetic_database(words, output_stream):    
    h = hyphenator()
    for word in words:
        syls = h.syllables(unicode(word))
        if len(syls) == 1: continue
        pairs = pair_with_next(syls)
        print pairs
        for (x,y) in pairs:
            print >>output_stream, x, y