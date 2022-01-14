# kapitell fra fra TEXT ANALYTICS WITH PYTHON

import pandas as pd
import numpy as np
import re
import nltk
import matplotlib.pyplot as plt

pd.options.display.max_colwidth=200

# %matplotlib inline

# building a corpus of text documents

corpus=["The sky is blue and beautiful.",
        "Love this blue and beautiful sky!",
        "The quick brown fox jumps over the lazy dog.",
        "A king's breakfast has sausages, ham, bacon, egg, toast and beans.",
        "The brown fox is quick and the blue dog is lazy!",#
        "The sky is very blue and the sky is very beautiful today",
        "The dog is lazy but the brown fox is quick!"]

labels=['weather','weather','animals','food','animals','weather','animals']

corpus=np.array(corpus)
corpus_df=pd.DataFrame({'Document':corpus,'Category':labels})

corpus_df=corpus_df[['Document','Category']]

wpt=nltk.WordPunctTokenizer()
stop_words=nltk.corpus.stopwords.words('english')


