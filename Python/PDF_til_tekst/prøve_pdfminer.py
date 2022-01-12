# Testing og utprøving av modulen PyPDF2

import os
import re
from pdfminer.high_level import extract_text

os.chdir('/home/bw/GitHub/Oppgaver/Python/PDF_til_tekst/')

filer=os.listdir()

pld_pdf=re.compile(r'(LNG_[0-9]{8}).pdf')
plattsrapporter=list(filter(pld_pdf.match,filer))


# PLD20211115=extract_text('LNG_20211115.pdf')




