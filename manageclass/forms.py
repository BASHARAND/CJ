from django import forms
from .models import has,Classroom,Course
FRUIT_CHOICES= [
    ('Sunday ','Sunday'),
    ('Mon', 'Mon'),
    ('Tus','Tus'),
    ('Wed','Wed'),
    ('Ther','Ther')
    ]

class Fill(forms.Form):
     Class = forms.ModelChoiceField(queryset=Classroom.objects.all())
     Cours = forms.ModelChoiceField(queryset=Course.objects.all())
     favorite_fruit= forms.CharField(label='What is your favorite fruit?', widget=forms.Select(choices=FRUIT_CHOICES))


     a=forms.BooleanField(initial=False,label = 'F',required=False)
     b = forms.BooleanField(initial=False,required=False)
     c=forms.BooleanField(initial=False,label='',required=False)
     d = forms.BooleanField(initial=False,label='',required=False)
     e = forms.BooleanField(initial=False,label='',required=False)
     f = forms.BooleanField(initial=False,label='',required=False)
     g = forms.BooleanField(initial=False,label='',required=False)
     h = forms.BooleanField(initial=False,label='',required=False)
     m = forms.BooleanField(initial=False,label='',required=False)
     n = forms.BooleanField(initial=False,label='',required=False)
     l = forms.BooleanField(initial=False,label='',required=False)
     w = forms.BooleanField(initial=False,label='',required=False)


