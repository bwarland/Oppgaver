
# side 12
import nltk
import spacy
import numpy as np
import pandas as pd

nlp=spacy.load('en_core_web_sm')


# spacy-model-en_core_web_sm-2.3.1
# nlp=spacy.load('en_core_web_sm',parse=True,tag=True,entity=True)
# conda install conda-forge spacy-model-en_core_web_sm

# side 13
sent1="The quick brown fox jumps over the lazy dog"
sent2="The brown fox is quick and he is jumping over the lazy dog"

ord1=sent1.split()
ord2=sent2.split()

pos_tags1=nltk.pos_tag(sent1.split())
pos_tags2=nltk.pos_tag(sent2.split())

SG1=pd.DataFrame(pos_tags1).T
SG2=pd.DataFrame(pos_tags2).T

# side 19
grammar='''
NP: {<DT>?<JJ>?<NN.*>}
AJDP: {<JJ>}
ADVP: {<RB.*>}
PP: {<IN>}
VP: {<MD>?<VB.*>+}
'''

pos_tagged_sent1=nltk.pos_tag(sent1.split())

rp1=nltk.RegexpParser(grammar)

pos_tagged_sent1=nltk.pos_tag(sent1.split())
pos_tagged_sent2=nltk.pos_tag(sent2.split())


# shallow_parsed_sent1=rp1.parse(pos_tagged_sent1)
# shallow_parsed_sent2=rp1.parse(pos_tagged_sent2)

print(shallow_parsed_sent1)
print(shallow_parsed_sent2)

# side 26
from spacy import displacy

displacy.render(nlp(sent2),
                jupyter=True,
                options={'distance':100,
                         'arrow_stroke':1.5,
                         'arrow_width':8})

from nltk.parse.stanford import StanfordParser
