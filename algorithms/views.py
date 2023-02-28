from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "algorithms/index.html")

# Create your views here.
def djikstras(request):
    return render(request, "algorithms/djikstras.html")

# Create your views here.
def sortingalgos(request):
    return render(request, "algorithms/sorting-algos.html")

# Create your views here.
def searchingalgos(request):
    return render(request, "algorithms/searching-algos.html")