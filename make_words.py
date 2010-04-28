#!/usr/bin/env python
from markov import Chain
import random

class WordGen(object):
    def __init__(self):
        """Reads in phonetic data and creates a markov chain"""
        data = []
        for x in open('data/phonmap.txt').readlines():
            data.extend(x.split())

        #Build up a markov chain with it
        self.chain = Chain(data, 2)
    
    def make_word(self):
        """Constructs words"""
        fragments = self.chain.generate(random.randint(2, 6))
        return "".join(fragments)

#Make words!
def main():
    gen = WordGen()
    words = [gen.make_word() for i in xrange(30)]
    print ", ".join(words)

main() if __name__ == '__main__' else None
