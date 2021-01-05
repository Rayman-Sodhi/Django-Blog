from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
     model= Post
     fields=('title' ,'title_tag','author','body','header_image')
     widgets={
         'title':forms.TextInput(attrs={'class':'forms-control'}),
         'title_tag': forms.TextInput(attrs={'class': 'forms-control'}),
         #'author': forms.Select(attrs={'class': 'forms-control'}),
         'author': forms.TextInput(attrs={'class': 'forms-control','value':'','id':'elder','type':'hidden'}),
         'body': forms.Textarea(attrs={'class': 'forms-control'}),

     }
class EditForm(forms.ModelForm):
    class Meta:
     model= Post
     fields=('title' ,'title_tag','body')
     widgets={
         'title':forms.TextInput(attrs={'class':'forms-control'}),
         'title_tag': forms.TextInput(attrs={'class': 'forms-control'}),
        # 'author': forms.Select(attrs={'class': 'forms-control'}),
         'body': forms.Textarea(attrs={'class': 'forms-control'}),

     }
