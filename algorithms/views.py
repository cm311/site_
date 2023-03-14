from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "algorithms/index.html")

def djikstras(request):
    return render(request, "algorithms/djikstras.html")

def sortingalgos(request):
    return render(request, "algorithms/sorting-algos.html")

def linearsearch(request):
    return render(request, "algorithms/linear-search.html")

def binarysearch(request):
    return render(request, "algorithms/binary-search.html")