# Utvalgte oppgaver fra HDTP løst i Python


# ,----
# | AUX - nth_element: N a_list -> N
# `----
# tar en liste og et nummer og returnerer et nummer
# Denne funksjonen er synes meg å være overflødig i Python.

def nth_element(a_list,N):
    return a_list[(N-1)]


# ,----
# | AUX - list_half: a_list string -> a_list
# `----
# Denne funksjonen tar enten første, eller andre halvdel av en liste.
# Jeg har skrevet denne funksjonen med en lambdakonstruksjon, noe som ikke
# anbefales. Min rasjonale er at jeg trengte en hjelpefunksjon, men syntes
# en full indre definisjonsfunksjon ble litt for mye for en så enkel funksjon
# som jeg trengte. For meg er dette en grei bruk av lambda slik jeg forstår det.

def list_half(a_list,half):
    """ Denne funksjonen tar en liste og en streng ("first" eller "last")
    """
    is_odd=lambda x: x%2==1
    list_length=len(a_list)
    halfway=(list_length//2) if is_odd(list_length) else (list_length/2)
    if half=='first':
        return a_list[:halfway]
    elif half==('last' or 'second'):
        return a_list[halfway:]
    
        
