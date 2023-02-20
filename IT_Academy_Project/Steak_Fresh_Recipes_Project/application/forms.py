from tkinter import Widget
from tkinter.tix import Form
from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class AddPost(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.Textarea(attrs={"class":"myfield"}))
    ingridients = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={"class":"myfield"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"class":"myfield"}))

    def clean_title(self):
        ttl_data = self.cleaned_data["title"]

        if ttl_data == "":
            raise ValidationError("The text shouldn`t be empty")
        return ttl_data
    
    def clean_ingridients(self):
        ingr_data = self.cleaned_data["ingridients"]

        if ingr_data == "":
            raise ValidationError("The text shouldn`t be empty")
        return ingr_data
    
    def clean_content(self):
        con_data = self.cleaned_data["content"]

        if con_data == "":
            raise ValidationError("The text shouldn`t be empty")
        return con_data
    
