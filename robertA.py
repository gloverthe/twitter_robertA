from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer
from transformers import AutoConfig, AutoModel
import numpy as np
from scipy.special import softmax
import csv
import urllib.request
import os
from functions.sqLiteFuncs import *
import pandas as pd
# @inproceedings{rosenthal2017semeval,
#   title={SemEval-2017 task 4: Sentiment analysis in Twitter},
#   author={Rosenthal, Sara and Farra, Noura and Nakov, Preslav},
#   booktitle={Proceedings of the 11th international workshop on semantic evaluation (SemEval-2017)},
#   pages={502--518},
#   year={2017}
# }
#


# Preprocess text (username and link placeholders)
def preprocess(text):
    new_text = []


    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)


# Tasks:
# emoji, emotion, hate, irony, offensive, sentiment
# stance/abortion, stance/atheism, stance/climate, stance/feminist, stance/hillary
task='sentiment'

#config = AutoConfig.from_pretrained('cardiffnlp/twitter-roberta-base-sentiment')
#MODEL = AutoModel.from_config(config)
MODEL = 'cardiffnlp'
#MODEL = os.path.join('cardiffnlp', 'twitter-roberta-base-sentiment')

tokenizer = AutoTokenizer.from_pretrained(MODEL)

#tokenizer.save_pretrained('cardiffnlp')
#config.save_pretrained('cardiffnlp')

# download label mapping
labels=[]
mapping_link = f"https://raw.githubusercontent.com/cardiffnlp/tweeteval/main/datasets/{task}/mapping.txt"
with urllib.request.urlopen(mapping_link) as f:
    html = f.read().decode('utf-8').split("\n")
    csvreader = csv.reader(html, delimiter='\t')
labels = [row[1] for row in csvreader if len(row) > 1]
print(labels)

# PT
model = AutoModelForSequenceClassification.from_pretrained(MODEL)
model.save_pretrained(MODEL)



#text = "@santanderukhelp Because as soon as you tell your problem they send links which have nothing to do with the problem"
def runModel(tweet):
    text = preprocess(tweet)
    encoded_input = tokenizer(text, return_tensors='pt')
    output = model(**encoded_input)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    ranking = np.argsort(scores)
    ranking = ranking[::-1]
    return labels[ranking[0]]

# for i in range(scores.shape[0]):
#     l = labels[ranking[i]]
#     s = scores[ranking[i]]
#     print(f"{i+1}) {l} {np.round(float(s), 4)}")

#print(runModel("@santanderukhelp Because as soon as you tell your problem they send links which have nothing to do with the problem"))

def robertA():
    engine = sqliteConnect(EnvConstants.sqlDBPath)
    noSent = pd.read_sql(sqlliteQ.getNoSent, engine)
    print(noSent)
    engine.close()
    noSent['sentiment'] = noSent.apply(lambda row:  runModel(row['text']),axis = 1)
    print(noSent)
    print(noSent.describe())
    appendToSQLliteNoUser(noSent)