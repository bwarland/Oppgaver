
from fractions import Fraction
import itertools, random


def P(event, space):
    "Sannsynlighet for en hendelse gitt et sample space"
    return Fraction(cases(favorable(event, space)),
                    cases(space))

favorable=set.intersection
cases=len

D={1,2,3,4,5,6}
even={2,4,6}

P(even,D)

prime={2,3,5,7,9,11,13}
odd={1,3,5,7,9,11,13}

suits=u'♥♠♦♣'
ranks=u'AKQJT98765432'

deck=[r+s for r in ranks for s in suits]

len(deck)

def combos(items, n):
    "alle kombinasjoner av n-antall elementer"
    return set(map(' '.join, itertools.combinations(items,n)))

Hands=combos(deck,5)
len(Hands)

