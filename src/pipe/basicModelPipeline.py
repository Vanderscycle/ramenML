import pandas as pd
import numpy as np
import pickle
import os 
import pickle
import sys
sys.path.insert(0,os.path.abspath('../helper'))
# matplotlib and seaborn causes the custom pandas import to fail...idk why so I commented them out
from customPandas import *

import argparse
import json

# importing the NN model
modelPath = os.path.abspath('../models/')
filename = 'veryBasicModelMK1.sav'
loaded_model = pickle.load(open(f'{modelPath}/{filename}', 'rb'))

def noodleRating(djangoDict):
    newSeries = pd.Series(djangoDict)
    return loaded_model.predict([newSeries])
# https://stackoverflow.com/questions/39491420/python-jsonexpecting-property-name-enclosed-in-double-quotes
#* json needs to use ("") and not ('')


#! https://stackoverflow.com/questions/988228/convert-a-string-representation-of-a-dictionary-to-a-dictionary
# test = """{"Brand":"Master Kong","Variety":"Onion Soy sauce prawn ramyun","Style":"tray","Country":"Japan"}"""
parser = argparse.ArgumentParser(description='Please pass a dictionary')
parser.add_argument('-i','--input',metavar='input',type=json.loads, help='Keys: brand,variety,style,country')
args = parser.parse_args()
# args = parser.parse_args(['-i', test])
sys.stdout.write(str(noodleRating(args.input)))
sys.stdout.flush()
sys.exit(0)