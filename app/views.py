from django.shortcuts import render, HttpResponse, redirect
from .models import Galary
from .forms import GalaryForm
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import GalarySerializer
# Create your views here.
def home(request):
    image = Galary.objects.all()
    context = {
        'image':image
    }

    return render(request, 'home.html', context)

def add(request):
    image = Galary.objects.all()
    form = GalaryForm()
    if request.method == 'POST':
        form = GalaryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {
        'form':form,
        'image':image
    }
    return render(request,'add.html', context)

def crudlist(request):
    image = Galary.objects.all()
    context = {
        'image':image
    }
   

    return render(request, 'crudlist.html', context)


def edit(request,iid):
   
    fruits = Galary.objects.get(pk=iid)
    form = GalaryForm(instance=fruits)

    if request.method == 'POST':
        form = GalaryForm(request.POST, instance=fruits)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'fruits': fruits,
        'form': form,
    }
    return render(request, 'edit.html', context)


    

def delete(request,iid):
    e=Galary.objects.get(pk=iid)
    e.delete()

    return redirect('/')


class GalaryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Galary.objects.all()
    serializer_class = GalarySerializer
    permission_classes = [permissions.IsAuthenticated]