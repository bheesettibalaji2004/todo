from django import forms
from .models import *

class SampleForm(forms.ModelForm):
    title = forms.CharField(label="",widget=forms.TextInput(attrs={"class":"form-control mb-3","placeholder":"enter title"}))
    description = forms.CharField(label="",widget=forms.Textarea(attrs={"class":"form-control","rows":3}))
    class Meta:
        model = Db
        fields = ("title","description")