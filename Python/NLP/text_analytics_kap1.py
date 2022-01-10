# kapitell en fra TEXT ANALYTICS WITH PYTHON

import nltk
import spacy
import numpy as np
import pandas as pd
# import en_core_web_sm

# hva gjør dette (ser ut til å virke)
# import spacy.cli
# spacy.cli.download('en_core_web_sm')

# nlp=en_core_web_sm.load()

# from spacy.lang.en import English
# nlp=English()


S1="The brown fox is quick and he is jumping over the lazy dog"

words=S1.split()

pos_tags=nltk.pos_tag(S1.split())

DR1=pd.DataFrame(pos_tags).T

spacy_pos_tagged=[(word,word.tag_,word.pos_) for word in nlp(S1)]

DR2=pd.DataFrame(spacy_pos_tagged).T

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

