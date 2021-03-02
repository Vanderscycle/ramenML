from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request,*args, **kwargs):
    """
    Home page view (not sure what to display yet)
    """
    return render(request,'home.html',{})
# we want to add a quick story
def about_view(request,*args, **kwargs):
    """
    page view to display the author of the model
    """
    context = {
        'author1':'Henri Vandersleyen',
        'github1':'https://github.com/Vanderscycle',
        'author2':'Olivia Kim',
        'github2':'https://github.com/yjik122'
    }
    return render(request,'about.html',context)


