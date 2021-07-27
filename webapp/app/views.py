from django.shortcuts import render
from wolframalpha.wolf import wolframAlpha

# Create your views here.


def results(request):
    x = wolframAlpha()
    x.doItAll(request)
    return render(request, "templates/results.html",{})