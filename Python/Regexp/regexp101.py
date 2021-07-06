#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 11:42:31 2020

@author: bwarland
"""

import re

# list(dir(re))

text_to_search='''

abcdefghijklmnopqrstuvwxyz
# lowcase_alpha='abcdefghijklmnopqrstuvwxyz'
# lowcase_alpha.upper()
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped)
.^$*+?{}[]\|()
coreyms.compile
321-555-4321
123.555.1234

Mr. Schafer
Mr Smith
Ms Davies
Mrs Robinson 
Mr. T


'''
 
sentence='Start a sentence and then bring it to an end.'

emails='''
bjorwa@equinor.com
bjorwa@statoil.com
bwarland@gmail.com
bjorwa@googlemail.com
bwarland@hotmail.com
bwarland@online.no
'''

rapporter='''
li200501.pdf
li20200815.pdf
LNG_20150101.pdf
LNG_20200531.pdf
200101lngd.pdf
heren-lmd-pdf-20200701.pdf
heren-glm-pdf-20200514.pdf
Global LNG Markets 14 Feb 2019.pdf


Floating LNG NG161.pdf
Gas in Europe NG2.pdf
Gas in Asia NG15.pdf
Gas in Americas_NG45.pdf
Gas in Africa NG65.pdr
20160101 ELNG.pdf
20200101 ELNG.pdf
180123 ELNG.pdf
20200310 PFELNG.pdf
'''
'''
(li|LNG_|heren-(lmd|glm)-pdf-)[0-9]{6,8}|[0-9]{6}lngd)|(Global LNG Markets [0-9]{2} [a-zA-Z]{3} [0-9]{4})
'''


# pattern=re.compile(r'((li|LNG_|heren-(lmd|glm)-pdf-)[0-9]{6,8}|[0-9]{6}lngd)|(Global LNG Markets [0-9]{2} [a-zA-Z]{3} [0-9]{4}\.pdf)')
# mønster=re.compile(r'.*[^a-zA-Z0-9]-?NG\d\d?\d?.pdf')
mønster=re.compile(r'[0-9]{6,8} ELNG.pdf')
rapporter=list(mønster.findall(rapporter))


# matches=pattern.findall(rapporter)



# for match in matches:
#     print(match)
