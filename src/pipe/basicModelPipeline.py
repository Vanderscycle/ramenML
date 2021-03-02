import pandas as pd
import numpy as np
import pickle
import os 
import pickle
import sys
sys.path.insert(0,os.path.abspath('../helper'))
# matplotlib and seaborn causes the custom pandas import to fail...idk why so I commented them out
from customPandas import *
from nltk.corpus import stopwords
import string
import argparse
import json

def nltkPreprocess(text):
    """
    Description:
        - Takes a text and cleans it by removing useless punctuations and stopwords
    input:
        -string
    output:
        - list of strings
    """
    # lower
    words = text.lower().split()
    # remove punctiuation
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in words]
    #remove stopwords
    stop_words = set(stopwords.words('english'))
    clean = [w for w in stripped if not w in stop_words if len(w)>2]
    return clean 


def cleanVariety(col):
    """
    description:
        - adaptation for 
    """
    cleanCol = list()
    # print(col)
    for v in col:
        # print(type(v))
        cleanCol.append(nltkPreprocess(v[0]))
    return col

# we are trying to make feature engineering part of our pipeline
from sklearn.preprocessing import FunctionTransformer
from sklearn.compose import ColumnTransformer
#! because the way .fit works in sklearn it passes the arrays as np.array so you must specify
mapper = ColumnTransformer(transformers=[
('Variety', FunctionTransformer(cleanVariety, validate=False),[1])], remainder='passthrough')

# importing the NN model
modelPath = os.path.abspath('../models/')
filename = 'veryBasicModelMK1.sav'
loaded_model = pickle.load(open(f'{modelPath}/{filename}', 'rb'))

def noodleRating(djangoDict):
    print(djangoDict)
    newSeries = pd.Series(djangoDict)
    return loaded_model.predict([newSeries])

# test data
# newRandoData ={ 
#     'Brand':'Master Kong',
#     'Variety':'Onion Soy sauce sour kimchi prawn ramyun',
#     'Style':'cup',
#     'Country': 'Japan'
# }
# newSeries = pd.Series(newRandoData)
# print(loaded_model.predict([newSeries]))
#! https://stackoverflow.com/questions/988228/convert-a-string-representation-of-a-dictionary-to-a-dictionary
test = "{'Brand':'Master Kong','Variety':'Onion Soy sauce sour kimchi prawn ramyun','Style':'cup','Country':'Japan'}"
print(json.loads(test))
parser = argparse.ArgumentParser(description='Please pass a dictionary')
parser.add_argument('-i','--input',metavar='input',type=json.load, help='Keys: brand,variety,style,country')
# args = parser.parse_args()
args = parser.parse_args(['-i', test])
# sys.stdout.write(noodleRating(args.input))
# sys.stdout.flush()
# sys.exit(0)