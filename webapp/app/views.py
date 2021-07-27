from django.shortcuts import render
from wolframalpha.wolf import wolframAlpha

# Create your views here.


def results(request):
    x = wolframAlpha()
    x.doItAll(request.POST['question'])
    return render(request, "templates/results.html",{})


def home(request):
    return render(request, "templates/home.html",{})