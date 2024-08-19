from django import forms
from django.forms import ModelForm
from . models import Note

class NoteForm(ModelForm):
    title = forms.CharField(max_length=200,widget=forms.TextInput(attrs={
            "class":"form-control","placeholder":"Enter Title"
        }))
    text = forms.CharField(max_length=10000,widget=forms.Textarea(attrs={
            "class":"form-control","placeholder":"Enter Text","rows":"8"
        }))
    class Meta:
      
        model = Note
        fields = ['title','text']