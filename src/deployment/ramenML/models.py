from django.db import models
import json
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent.parent

with open(f'{BASE_DIR}/models/DjangoRamenMLDropDownVals.json','rb') as fp:
    jsonData = json.load(fp)

# for key, valueList in jsonData.items():
#     print([(value,value) for value in valueList[:5]])
#     print (key)


def jsonDjangoTupple(jsonData):
    """
    Django only takes tuples (actual value, human readable name) so we need to repack the json in a dictionay of tuples
    """
    dicOfTupple = dict()
    for key, valueList in jsonData.items():
        dicOfTupple[str(key)]=[(value,value) for value in valueList]
    return dicOfTupple

json_data = jsonDjangoTupple(jsonData)
# Create your models here.
class NewRamen(models.Model):
    brand = models.CharField(max_length=120,choices=json_data['Brand'], default='Nissin')
    style = models.CharField(max_length=120,choices=json_data['Style'], default='Pack')
    country = models.CharField(max_length=120,choices=json_data['Country'], default='Japan')
    ingredients = models.CharField(max_length=120, default='Soy')