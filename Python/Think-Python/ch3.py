# FUNKSJONER

# ,----
# | 3-1 right_justify: S N -> S
# `----
# tar en streng/tekst og nummer og justerer streng/tekst mot høyre N plasser

def right_justify(tekst, spaces):
    return spaces*' ' + tekst

def do_twice(f):
    f()
    f()

def print_spam():
    print('spam')
    
# ,----
# | 3-3 grid: ... -> S
# `----
# tegn en enkel grid
# ekstraoppgave: gjøre denne generell basert og basert på antall ruter

def print_beam():
    print('+-----+-----+')
    
def print_between():
    print('|     |     |')

def grid():
    for i in range(0,2):
        print_beam()
        for j in range(0,4):
            print_between()
    print_beam()
