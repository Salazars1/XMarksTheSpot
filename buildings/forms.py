from django import forms

class ReservationForm(forms.Form):
    day = forms.CharField(label='Day: ', max_length=10)
    time = forms.IntegerField(label='Time: ', max_value=23)