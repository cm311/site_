from django.shortcuts import render
from django.http import HttpResponse
from little_lemon.forms import *
from little_lemon.models import Menu

# Create your views here.
def home(request):
    return render(request, 'little_lemon/home.html')

def about(request):
    return render(request, 'little_lemon/about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'little_lemon/book.html', context)

def menu(request):
    items = {'menu' : Menu.objects.all()}
    return render(request, 'little_lemon/menu.html', items)

def display_menu_item(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ""
    return render(request, 'little_lemon/menu_item.html', {'menu_item' :menu_item})


def form_view(request):
    form = ShiftLoggerForm()

    if request.method == 'POST':
        form = ShiftLoggerForm(request.POST)
        if form.is_valid():
            form.save()

    context = {"form" : form}
    print(context)
    return render(request, 'little_lemon/home.html', context)

def booking_form_view(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form" : form}
    return render(request, "little_lemon/booking.html", context)

