# Testing og utprøving av modulen PyPDF2

import os
from pdfminer.high_level import extract_text

os.chdir('/home/bw/GitHub/Oppgaver/Python/PDF_til_tekst/')

PLD20211115=extract_text('LNG_20211115.pdf')

Dette fungerer ganske greit, men må tenke litt gjennom hva jeg gjør med teksten (skrive ut i tekstfiler kanskje?)
