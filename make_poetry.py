#!/usr/bin/env python
from markov import Chain
import re

poem = """

Jack Sprat could eat no fat
His wife could eat no lean
And so betwixt the two of them
They licked the platter clean

Jack ate all the lean,
Joan ate all the fat.
The bone they picked it clean,
Then gave it to the cat

Jack Sprat was wheeling,
His wife by the ditch.
The barrow turned over,
And in she did pitch.

Says Jack, "She'll be drowned!"
But Joan did reply,
"I don't think I shall,
For the ditch is quite dry.".

The Grand old Duke of York he had ten thousand men
He marched them up to the top of the hill
And he marched them down again.
When they were up, they were up
And when they were down, they were down
And when they were only halfway up
They were neither up nor down. 
"""

 
def tokens(text):
    return [x.lower() for x in re.split(r'(\W+)', text)]
 
def main():
    chain = Chain(tokens(poem), 4)
    words = chain.generate(2000)
    print ''.join([x for x in words])

main() if __name__=='__main__' else None