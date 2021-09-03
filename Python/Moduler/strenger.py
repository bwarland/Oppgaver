import string

# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.digits)
# print(string.hexdigits)
# print(string.octdigits)
# print(string.punctuation)
# print(string.printable)
# print(string.whitespace)

# '{0},{1},{2}'.format('a','b','c')
# '{0}{1}{0}'.format('abra','cad') # => 'abracadabra'
# '{0},{1},{0}'.format('a','b','c') # => 'a,b,a'

eks1="Monthy Python's Flying Cirus"
abra="abra cadabra"

# print(eks1.upper())
# print(eks1.lower())
# print(eks1.split()) # => skriver ut til liste
# print(eks1.replace("Python","Ananconda"))

# print(string.capwords(abra))

# formatter=string.Formatter()

# print(formatter.format('{website}',website='JournalDev'))
# print(formatter.format('{} {website}','Welcome to',website='JournalDev'))
# print('{} {website}'.format('Welcome to',website='JournalDev'))

# print(abra.count('a')) # => 5
print(abra[::-1])
print(abra[::])
print(abra[1::])
zip_test=zip(abra[::],abra[1::])
