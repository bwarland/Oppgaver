# dictionaries

# ,----
# | histogram: string -> dictionary
# `----

def histogram(string):
    dictionary={}
    L_case_string=string.lower()
    for letter in L_case_string:
        if letter not in dictionary:
            dictionary[letter]=1
        else:
            dictionary[letter]+=1
    return dictionary

assert histogram('Mississippi')=={'m': 1, 'i': 4, 's': 4, 'p': 2}
