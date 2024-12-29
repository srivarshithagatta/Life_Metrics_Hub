from django import forms

class AgeCalculatorForm(forms.Form):
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), label="Date of Birth")
    current_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), label="Current Date")
