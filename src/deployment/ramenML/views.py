from django.shortcuts import render
from django.http import HttpResponse

import sys
import os
import pickle
import subprocess
from pathlib import Path
import json
#se the path to the model
BASE_DIR = Path(__file__).resolve().parent.parent
pipelineScripts = os.path.join(BASE_DIR.parent,'pipe/') 
modelUsed = 'basicModelPipeline.py'
# subprocess.call(["python", pipelineScripts + modelUsed,'-i'])

from .forms import NewRamenForm
# # Create your views here.
def ramenModel_create_view(request,*args, **kwargs):
    form = NewRamenForm(request.POST or None)
    results = None
    

    if form.is_valid():
        print(form.cleaned_data)
        # https://stackoverflow.com/questions/1996518/retrieving-the-output-of-subprocess-call
        predictedRating = subprocess.check_output(["python", pipelineScripts + modelUsed,'-i',json.dumps(form.cleaned_data)], stderr=subprocess.STDOUT).decode()
        print(predictedRating)
        # print(results)
        context = {
        'form' :form,
        'results': predictedRating     
            }
        return render(request,'ramenML.html',context)
    else:
        print(form.errors)
        # form.save()
    context = {
        'form' :form     
            }
    return render(request,'ramenML.html',context)