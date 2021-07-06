# Collections er datakontainere for lagring av data i tillegg
# til dem som er innebygd (list, dict, set, tuple)
import collections

# en underklasse av Python dictionary
from collections import Counter

# fungerer akkurat som en Python dictionary men den gir ingen feil når man
# spør etter elementer som ikke er i listen
from collections import defaultdict

# en python dictionary som holder orden alt etter når ting blir lagt inn
from collections import OrderedDict

# en liste som er optimalisert for endring (legge til og trekke fra)
from collections import deque

# en måte man kan sette sammen såkalte dictionaries
from collections import ChainMap

# denne gir navn til hver posisjon i en rekke
from collections import namedtuple

# cnt=Counter()

# liste1=[1,2,3,4,5,1,2,3,4,5,6,7,8,1,2,3,2,1]
# liste_frekvens=Counter(liste1)
# print(liste_frekvens[1])
# print(list(liste_frekvens.elements()))
# print(list(liste_frekvens.most_common()))
# trekk_fra={1:2,2:2}
# liste_frekvens.subtract(trekk_fra)
# print(liste_frekvens)

liste2=['a','b','c','a','b','a','c','a']
deq=deque(liste2)
print(deq)
deq.append('d')
deq.appendleft('e')
print(deq)
# deq.pop()
# deq.clear()
# print(deq.count('a'))

dict1={'a':1,
       'b':2,
       'c':3}
dict2={'d':4,
       'e':5,
       'f':6}

chain_map=ChainMap(dict1,dict2)
print(chain_map.maps)

student=namedtuple('student','fornavn, etternavn, alder')
s1=student('Magnus','Warland','20')
s2=student('Theo','Warland','8')
print(s2)
