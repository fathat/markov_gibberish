#!/usr/bin/env python
from markov import Chain
import re

poem = """
Good night, sleep tight,
Don't let the bedbugs bite.
And if they do
Then take your shoe
And knock 'em 'til
They're black and blue!

Baa, baa black sheep
Have you any wool
Yes sir, yes sir
Three bags full.

One for my master
And one for my dame
And one for the little boy
Who lives down the lane.


The Sandman's coming in his train of cars
With moonbeam windows and with wheels of stars
So hush you little ones and have no fear
The man-in-the-moon he is the engineer

The railroad track tis a moonbeam bright
That leads right up into the starry night

So put on you 'jamas and say your prayers
"""

 
def tokens(text):
    return [x.lower() for x in re.split(r'(\W+)', text)]
 
def main():
    chain = Chain(tokens(poem), 4)
    words = chain.generate(2000)
    print ''.join([x for x in words])

main() if __name__=='__main__' else None