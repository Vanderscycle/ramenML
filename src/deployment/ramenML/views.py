from django.shortcuts import render
from django.http import HttpResponse

from .forms import NewRamenForm
# Create your views here.
def ramenModel_create_view(request,*args, **kwargs):
    form = NewRamenForm(request.POST or None)
    results = None
    

    if form.is_valid():
        print(form.cleaned_data)
        context = {
        'form' :form,
        'results':form.cleaned_data        
            }
        return render(request,'ramenML.html',context)
    else:
        print(form.errors)
        # form.save()
    context = {
        'form' :form     
            }
    return render(request,'ramenML.html',context)