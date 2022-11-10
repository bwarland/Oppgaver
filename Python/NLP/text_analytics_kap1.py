# kapitell en fra TEXT ANALYTICS WITH PYTHON

import nltk
nltk.download('averaged_perceptron_tagger')
import spacy
import numpy as np
import pandas as pd
# import en_core_web_sm

# hva gjør dette (ser ut til å virke)
# import spacy.cli
# spacy.cli.download('en_core_web_sm')

# nlp=en_core_web_sm.load()

# Denne ser ut til å løse med det problemet at en_core_web_sm ikke laster
# men jeg husker dessverre ikke hvor jeg fant denne løsningen
from spacy.lang.en import English
nlp=English()


S1="The brown fox is quick and he is jumping over the lazy dog"
S2="The quick brown fox jumps over the lazy dog"

W1=S1.split()
W2=S2.split()

pos_tags1=nltk.pos_tag(S1.split())
pos_tags2=nltk.pos_tag(S2.split())

DR1=pd.DataFrame(pos_tags1).T

DR2=pd.DataFrame(pos_tags2).T

spacy_pos_tagged=[(word,word.tag_,word.pos_) for word in nlp(S1)]

DR3=pd.DataFrame(spacy_pos_tagged).T

grammar='''
        NP:{<DT>?<JJ>?<NN.*>}
        ADJP: {<JJ>}
        ADVP: {<RB.*>}
        PP: {<IN>}
        VP: {<MD>?<VB.*>+}
        '''

pos_tagged_sent=nltk.pos_tag(S1.split())
rp=nltk.RegexpParser(grammar)

shallow_parsed_sent=rp.parse(pos_tagged_sent)
# print(shallow_parsed_sent)

######################
from nltk.parse.stanford import StanfordParser

