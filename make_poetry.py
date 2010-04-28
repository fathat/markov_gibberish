#!/usr/bin/env python
from markov import Chain
import re

poem = """
Bye, baby bunting
Daddy's gone a hunting
To get a little rabbit skin
To wrap his baby bunting in
Bye, baby bunting
Daddy's gone a hunting
To get a little lambie skin
To wrap his baby bunting in
Bye, baby bunting
Daddy's gone a hunting
A rosy wisp of cloud to win
To wrap his baby bunting in

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