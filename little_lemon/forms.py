from django import forms
from little_lemon.models import ShiftLogger, Booking



class ShiftLoggerForm(forms.ModelForm):
    class Meta:
        model = ShiftLogger
        fields = '__all__'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'



