from django.shortcuts import render,redirect
from .import models
from .forms import Fill
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate


@login_required

def RegisterOrder(request):


    if request.method == 'GET':
        post1 = models.has.objects.filter(Class_id=1)
        post2 = models.has.objects.filter(Class_id=2)
        post3 = models.has.objects.filter(Class_id=3)

        post4 = models.has.objects.filter(Class_id=4)
        post5 = models.has.objects.filter(Class_id=5)
        post6 = models.has.objects.filter(Class_id=6)

        data = Fill

        return render(request, 'reg.html', {'formreg': data,'post1':post1,'post2':post2,'post3':post3,'post4':post4,'post5':post5,'post6':post6})
    else:



        data = Fill(request.POST)

        if data.is_valid():
            table = models.has()

            a = data.cleaned_data['Class']
            z=str(a)
            b = data.cleaned_data['Cours']
            z1=str(b)
            item = models.Classroom.objects.get(num=z)
            item1 = models.Course.objects.get(num=z1)


            table.Class = item
            table.course = item1
            table.day = data.cleaned_data['favorite_fruit']
            table.a=data.cleaned_data['a']
            table.b=data.cleaned_data['b']
            table.c=data.cleaned_data['c']
            table.d=data.cleaned_data['d']
            table.e=data.cleaned_data['e']
            table.f=data.cleaned_data['f']

            table.g=data.cleaned_data['g']
            table.h=data.cleaned_data['h']
            table.m=data.cleaned_data['m']
            table.n=data.cleaned_data['n']
            table.l=data.cleaned_data['l']
            table.w=data.cleaned_data['w']



            table.save()

        context = {
            'former': data
        }
        return redirect('/Reg/')



# Create your views here.
