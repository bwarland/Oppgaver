

# for i in [1,2,3,4,5]:
#     print(i)
#     for j in [1,2,3,4,5]:
#         print(j)
#         print(i+j)
#     print(i)
# print("done looping")

users=[
    {"id":0, "name":"Hero"},
    {"id":1, "name":"Dunn"},
    {"id":2, "name":"Sue"},
    {"id":3, "name":"Chi"},
    {"id":4, "name":"Thor"},
    {"id":5, "name":"Clive"},
    {"id":6, "name":"Hicks"},
    {"id":7, "name":"Devon"},
    {"id":8, "name":"Kate"},
    {"id":9, "name":"Klein"}]

# En liste med dictionaries, en dictionary for hver bruker. Er dette en vanlig
# måte å modere data på i Python? Samlet sett har ingen av såkalte dictionaries
# en unik identifikator, men hver dictionary blir identifisert av sin plass i listen.

friendship_pairs=[(0,1),
                  (0,2),
                  (1,2),
                  (1,3),
                  (2,3),
                  (3,4),
                  (4,5),
                  (5,6),
                  (5,7),
                  (6,8),
                  (7,8),
                  (8,9)]

# Dette er en liste med såkalte tuples, også en sammensatt datastruktur. Er også dette
# vanlig. Og hva er det i så fall som gjør denne til en bedre datastruktur enn en
# liste i en liste?

# Dette er et innledende kapitell, og hva ønsker forfatteren å få frem med dette?
# Kunne han ikke unngått å komme med så mye sammensatt informasjon ved å bruke en
# enklere datastruktur?

# lager en parliste med id og tomme lister
friendships={user["id"]:[] for user in users} 

# fyller inn de tomme listene
# men her forstår jeg ikke helt prossessen/logikken
for i, j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)

# list_of_lists=[[1,2,3],
#                [4,5,6],
#                [7,8,9]]

def friends(user):
    user_id=user["id"]
    friend_ids=friendships[user_id]
    return len(friend_ids)

total_connections=sum(friends(user) for user in users)
number_users=len(users)
average_connections=total_connections/number_users

import re
my_regex=re.compile("[0-9]+",re.I)

import matplotlib.pyplot as plt

from collections import defaultdict, Counter
lookup=defaultdict(int)
my_counter=Counter()



# Normalen i Python er slik at man introduserer en funksjonsdefinisjon med nøkkelordet def, men
# man har også muligheten til å gjøre dette med en variabeldeklarasjon som bruker en lambda-funksjon
# som vist nedenfor:

double=lambda x: 2*x
square=lambda x: x**2
sqrt=lambda x: x**(1/2)

# Dette tror jeg viser en grei måte å dokumentere i koden på:

def navn(første,andre):
    return første+" "+andre

fornavn="Theo"
etternavn="Warland"

fullt_navn_1=fornavn+" "+etternavn
fullt_navn_2="{0} {1}:".format(fornavn,etternavn)

# Denne her synes jeg er elegant
fullt_navn_3=f"{fornavn} {etternavn}"

familie=[["Theo","Warland"],
         ["Kelly","Warland"],
         ["Bjørn","Warland"]]

# Denne forstår jeg ikke helt i det at fornavn og etternavn automatisk plukker
# første og andre element i første element av listen. Er dette naturlig?
# Det er som om det er en form for listeintelligens i Python-språket.

# for fornavn,etternavn in familie:
#     print(f"{fornavn} {etternavn}")

# Denne her skriver ut alle elementene i listen, det vil si en ny liste med
# fornavn og etternavn
    
# for navn in familie:
#     print(navn)

    
tall=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
tall_to=[1,1,1,2,3,2,1,2,2,3,4,5,43,3,3,3,4,5,19]
rekke=1,2,3,4
enda_en_rekke=(1,2,3,4,4)

ordliste={}
karakter={"blaeh":0,"tom":3,"helge":5}

x=None
assert x is None

par=[(x,y) for x in range(10) for y in range(10)]
flere_par=[(-x,-y) for x in range(5) for y in range(5)]
mer_par=[(-x,y) for x in range(5) for y in range(5)]
dict_par=[{x:y} for x in range(10) for y in range(10)]

# Theo="Theo"
# Warland="Warland"

# fullt_navn=f"{Theo} {Warland}"

# fullt_navn=f"{Theo} {Warland}"+":"
