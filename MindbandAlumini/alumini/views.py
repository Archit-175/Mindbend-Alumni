from django.shortcuts import render

# Create your views here.
def alumini_page(request):
    return render(request,"alumini/alumini.html")