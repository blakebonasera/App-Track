from django import forms

class ImageForm(forms.Form):
    position = forms.CharField(max_length=50)
    company = forms.CharField(max_length=50)
    location = forms.CharField(max_length=25)
    url = forms.TextField()