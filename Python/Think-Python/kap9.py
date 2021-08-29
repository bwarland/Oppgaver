
# http://thinkpython2.com/code/words.txt

fin=open('words.txt')

fin.readline()

line=fin.readline()

word=line.strip()

# for line in fin:
#     word=line.strip()
#     print(word)


# lines_in_text: txt -> number
# returns the number of lines or words in a text

def lines_in_text(text):
    counter=0
    for line in text:
        counter=counter+1
    return counter

# 9-1
# skriv alle ord som er lengre enn bokstaver bokstaver

# for line in fin:
#     word=line.strip()
#     if len(word)>20:
#         print(word)
#     else:
#         pass

# 9-2
# funksjon som avgjør om ord har bokstaven E i seg eller ikke

def no_E_p(word):
    for letter in range(len(word)):
        if letter=='e':
            pass
        else:
            return True

        
    
