from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import NavigationRecordForm
from django.contrib import messages
from .models import NavigationRecord, Vehicle

def Index(request):
  return render(request, 'index.html')


def UpdateNavgation(request, id):
  evraka = get_object_or_404(NavigationRecord, id = id)
  form = NavigationRecordForm(request.POST or None, request.FILES or None,instance=expedition)
  if form.is_valid():
    evraka = form.save(commit=False)
    evraka.sofor = request.user
    evraka.save()
    messages.success(request,"Transfer başarıyla güncellendi.")
    return redirect('expedition:dashboard')

  return render(request, 'update.html', {"form":form})


def Dashboard(request):
  evraka = NavigationRecord.objects.filter(user=request.user)
  context = {
      'evraka':evraka,
  }
  return render(request, 'dashboard.html', context)

def addEvraka(request):
  form = NavigationRecordForm(request.POST or None)

  if form.is_valid():
    evraka = form.save(commit=False)

    evraka.user = request.user
    evraka.save()
    messages.success(request,"Transfer başarıyla oluşturuldu.")
    return redirect('evraka:dashboard')

  return render(request,'addexpedition.html',{"form":form})

def UpdateEvraka(request, id):
  expedition = get_object_or_404(NavigationRecord, id = id)
  form = NavigationRecordForm(request.POST or None, request.FILES or None,instance=expedition)
  
  if form.is_valid():
    evraka = form.save(commit=False)
    evraka.user = request.user
    evraka.save()

    messages.success(request,"Transfer başarıyla güncellendi.")
    return redirect('evraka:dashboard')

  return render(request, 'update.html', {"form":form})


def DeleteEvraka(request, id):
  evraka = get_object_or_404(NavigationRecord, id = id)
  evraka.delete()
  messages.warning(request,'Transfer başarıyla silindi.')
  return redirect('evraka:dashboard')
