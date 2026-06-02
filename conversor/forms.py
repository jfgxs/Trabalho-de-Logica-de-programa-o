from django import forms

class PDFForm(forms.Form):
    pdf = forms.FileField()