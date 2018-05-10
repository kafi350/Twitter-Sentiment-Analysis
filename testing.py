# Sneek peek on the results.
# Importing sentiment_mod module and then testing on some feeds and statements.

import sentiment_mod as senti
import pandas as pd
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from keras.preprocessing.text import Tokenizer
from tensorflow.contrib.gan.python import train
import re

print(senti.sentiment("He is an incapable person. His projects are totally senseless."))
print(senti.sentiment("This movie was awesome! The acting was great, plot was wonderful !"))
print(senti.sentiment("This movie was utter junk.. I don't see what the point was at all. Horrible movie, 0/10"))
print(senti.sentiment("He is a freak."))
print(senti.sentiment("Movie was nice. Actors did very well. All together a nice experience."))
print(senti.sentiment("Are you fucking mad ?"))
print(senti.sentiment("You are dumb."))

# data = pd.read_csv('D:\Thesis\Datasets\Amazon-reviews-unlocked-mobile-phones\Data.csv')
#
# data = data['Reviews']
#
# data['Reviews'] = data['Reviews'].apply(lambda x: str(x) if type(x)==float or type(x) == bool else x.lower())
# data['Reviews'] = data['Reviews'].apply((lambda x:  re.sub('[^a-zA-z0-9\s]', '', x)))
#
# print(data['Reviews'])




