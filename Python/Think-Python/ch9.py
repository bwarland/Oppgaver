# kapitell 9

fin=open('words.txt')


# ,----
# | OPPGAVE 9-1: finn ord over 20 bokstaver og skriv ut
# `----

def read_word(document):
    line=document.readline()
    word=line.strip()
    print(word)
    
# hvor mange ord i det engelske språk har mer enn 20 bokstaver?
# for word in fin:
#     if len(word)>20:
#         print(word)
#     else:
#         pass


# ,----
# | ,----
# | | OPPGAVE 9-2: hvor mange ord i engelsk bruker ikke bokstaven "e"
# | `----
# `----

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

assert has_no_e('abc')==True
assert has_no_e('dedf')==False


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

# for word in fin:
#     if includes('aeiou',word)==True:
#         print(word)
#     else:
#         pass

# ,----
# | ,----
# | | OPPGAVE 9-5: bruker et ord alle bokstaver?
# | `----
# `----


# ,----
# | ,----
# | | oppgave 9-6: kommer alle bokstaver i et ord i alfabetisk rekkefølge?
# | `----
# `----



