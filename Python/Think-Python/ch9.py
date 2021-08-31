# Kapitell 9: Spill Med Ord

fin=open('words.txt')


# ,----
# | OPPGAVE 9-1: finn ord over 20 bokstaver og skriv ut
# `----

def read_word(document):
    line=document.readline()
    word=line.strip()
    return word

# ,----
# | ordliste
# `----

# ordliste=[]

# for word in fin:
#     ordliste.append(word.strip())

# ord i det engelske språk som har mer enn 20 bokstaver?

# for word in fin:
#     if len(word)>20:
#         print(word)
#     else:
#         pass

# Men hvordan vil en funksjon se ut?

# letters_over_N: doc N -> string

def letters_over_N(document,N):
    for word in document:
        if len(word)>N:
            print(word)
        else:
            pass

# ,----
# | ,----
# | | OPPGAVE 9-2: hvor mange ord i engelsk bruker ikke bokstaven "e"
# | `----
# `----

# 1) funksjon: har et ord "e" i seg eller ikke?
# 2) skriv ut alle ord som ikke har "e" i seg
# 3) hvor stor andel av engelske ord har ikke "e" i seg?

# l_in_word: string -> *string
# prints letters in a word

# l_in_word: str -> str*
# skriver ut alle bokstaver i et ord

def l_in_word(w):
    num_l=len(w)
    for l in range(0,num_l):
        print(w[l])

# has_no_e: string -> boolean
# takes a string en determines if the string has a letter "e" in it
# denne gir feil resultat!!

# def has_no_e(word):
#     num_letters=len(word)
#     for index in range(0,num_letters):
#         if word[index]=="e":
#             return False
#         else:
#             return True

def has_no_e(w):
    for l in w:
        if l=='e':
            return False
    return True

# assert has_no_e('abc')==True
# assert has_no_e('dedf')==False


# lines_in_doc: document -> integer
# counts the number of lines (words in this case) in a document
# fin har 113783

def lines_in_doc(document):
    counter=0
    for lines in document:
        counter+=1
    return counter

# words_wo_e: document -> integer
# counts words withough the letter 'e'
# call to function has_no_e in process
# antall ord uten 'e': 109419
# 0.0383537083747133
def words_wo_e(document):
    counter=0
    for word in document:
        if has_no_e(word)==True:
            counter+=1
        else:
            pass
    return counter

# for w in fin:
#     if has_no_e(w):
#         print(w)
#     else:
#         pass

# 0.33069087649297346

# ,----
# | ,----
# | | OPPGAVE 9-3: har et ord gitte bokstaver i seg?
# | `----
# `----

# 1) en funksjon som tar et ord og en streng med bokstaver og vurderer om ordet har alle bokstavene i seg

# 2) en funksjon som tar en streng med bokstaver og skriver ut antallet ord som ikke har disse bokstavene i seg

# 3) hvilken kombinasjon av fem bokstaver ekskluderer færrest ord

# has_no_lettter: str str -> boolean
# checks if a letter can be found in word

def has_no_letter(l,w):
    for letter in w:
        if letter==l:
            return False
    return True

# assert has_no_letter('a','abcd')==False
# assert has_no_letter('b','abcd')==False
# assert has_no_letter('e','abcd')==True

# avoids: str str -> boolean
# takes a string of letters and a word (string) returns truth value

def avoids(letters, word):
    for l in letters:
        if has_no_letter(l,word)!=True:
            return False
    return True

# assert avoids('abc','abcdef')==False
# assert avoids('xyc','abcdef')==False
# assert avoids('zcy','abcdefgh')==False
# assert avoids('abc','defgij')==True

# Denne koden ser ut til å gjøre det den skal, men jeg synes prossessen er uttrykt litt klønete

# include: str str -> boolean
# checks if a word includes a letter

def include(L,W):
    for letter in W:
        if letter==L:
            return True
    return False

# assert include('a','abc')==True
# assert include('a','bca')==True
# assert include('w','abc')==False

# ,----
# | ,----
# | | OPPGAVE 9-4: hvilke ord har gitt sett med bokstaver
# | `----
# `----

# 1) funksjon: bruker et ord kun oppgitte bokstaver (streng)?
# 2) setning med bokstavene acefhlo?

# includes: str str -> boolean
# checks if word includes given letters

def includes(L,W):
    for letter in L:
        if include(letter,W)!=True:
            return False
    return True
        
# assert includes('ab','abc')==True
# assert includes('abc','xyzabc')==True
# assert includes('aw','abcd')==False
# assert includes('zyz','abcdefghij')==False

# ,----
# | ,----
# | | OPPGAVE 9-5: bruker et ord alle bokstaver?
# | `----
# `----

# 1) funksjon: bruker et ord alle gitte bokstaver minst en gang?
# 
# def all_letters(word,letters):
    

# 2) hvilket ord bruker alle bokstavene aeiou?

# for word in fin:
#     if includes('aeiou',word)==True:
#         print(word)
#     else:
#         pass

# 3) er det noen ord som bruker alle bokstavene aeiouy?

# for word in fin:
#     if includes('aeiouy',word)==True:
#         print(word)
#     else:
#         pass

# ,----
# | ,----
# | | oppgave 9-6: kommer alle bokstaver i et ord i alfabetisk rekkefølge?
# | `----
# `----

# alfabet='abcdefghijklmnopqrstuvwxyz'
# betalfa=alfabet[::-1]

# abc_p: string -> boolean
# vurderer om alle bokstaver i et ord kommer i alfabetisk rekkefølge 


# https://www.quora.com/How-do-I-iterate-through-a-list-in-python-while-comparing-the-values-at-adjacent-indices
# https://python-forum.io/thread-14284.html

def abc_p(et_ord):
    liten_b=et_ord.lower()
    sannhetsliste=[]
    for i,j in zip(liten_b[::],liten_b[1::]):
        sannhetsliste.append(i<=j)
    for verdi in sannhetsliste:
        # return True
        if verdi==False:
            break
    else:
        return True
    return False
     
# assert abc_p(alfabet)==True
# assert abc_p('Abc')==True
# assert abc_p(betalfa)==False
# assert abc_p('abcabc')==False

# ,----
# | word_in_english: document + function_p -> integer
# `----
# takes a document and a function (predicate) and returns a number

# def word_in_english(document,function_p):
#     teller=0
#     for word in document:
#         clean=word.strip() # strip tar vekk linjeskift
#         if function_p(clean) is True:
#             teller+=1
#         else:
#             pass
#     return teller

# assert word_in_english(fin,abc_p)==596

    
# ,----
# | ,----
# | | oppgave 9.7: ord med tre dobble bokstaver på rad
# | `----
# `----
# committee eller Mississippi kunne nesten vært eksempler



# ,----
# | ,----
# | | oppgave 9.8: palindromiske tall
# | `----
# `----



# ,----
# | ,----
# | | oppgave 9.9: dobbling av tall og reversering av tall
# | `----
# `----






