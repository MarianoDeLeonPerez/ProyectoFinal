from django import forms


class PeticionForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    autor=forms.CharField(max_length=50)

