from django.shortcuts import render

# Create your views here.

def index(request, *args, **kwargs):
    context = {}
    return render(request, "index.html", context=context)
