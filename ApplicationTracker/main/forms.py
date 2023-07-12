from django import forms

class ApplicationForm(forms.Form):
    position = forms.CharField(max_length=50)
    company = forms.CharField(max_length=50)
    location = forms.CharField(max_length=25)
    url = forms.CharField(widget=forms.Textarea)