
import nltk, spacy, numpy as np, pandas as pd



nlp=spacy.load('en_core_web_lg')

# nlp=spacy.load('en_core_web_sm',parse=True,tag=True,entity=True)
# conda install conda-forge spacy-model-en_core_web_sm


sent1="The quick brown fox jumps over the lazy dog"
sent2="The brown fox is quick and he is jumping over the lazy dog"

ord1=sent1.split()
ord2=sent2.split()

pos_tags1=nltk.pos_tag(sent1.split())
pos_tags2=nltk.pos_tag(sent2.split())

pd.DataFrame(pos_tags2).T


grammar='''
NP: {<DT>?<JJ>?<NN.*>}
AJDP: {<JJ>}
ADVP: {<RB.*>}
PP: {<IN>}
VP: {<MD>?<VB.*>+}
'''

pos_tagged_sent1=nltk.pos_tag(sent1.split())
rp1=nltk.RegexpParser(grammar)
shallow_parsed_sent1=rp1.parse(pos_tagged_sent1)
print(shallow_parsed_sent1)

