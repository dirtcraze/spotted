from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .forms import MessageForm
from .models import *

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def fitnessforlife(request):
  if request.method == 'POST':
    form = MessageForm(request.POST)
    if form.is_valid():
      message = form.cleaned_data['message']
      Fitnessforlife.objects.create(message=message)
      return render(request, 'template.html')
  else:
    form = MessageForm()
  return render(request, 'template.html', {'form': form})

def fitnesstrzykorony(request):
  if request.method == 'POST':
    form = MessageForm(request.POST)
    if form.is_valid():
      message = form.cleaned_data['message']
      Fitnesstrzykorony.objects.create(message=message)
      return render(request, 'template.html')
  else:
    form = MessageForm()
  return render(request, 'template.html', {'form': form})

def halnygym(request):
  if request.method == 'POST':
    form = MessageForm(request.POST)
    if form.is_valid():
      message = form.cleaned_data['message']
      Halnygym.objects.create(message=message)
      return render(request, 'template.html')
  else:
    form = MessageForm()
  return render(request, 'template.html', {'form': form})

def oxygym(request):
  if request.method == 'POST':
    form = MessageForm(request.POST)
    if form.is_valid():
      message = form.cleaned_data['message']
      Oxygym.objects.create(message=message)
      return render(request, 'template.html')
  else:
    form = MessageForm()
  return render(request, 'template.html', {'form': form})

def xtremefitness(request):
  if request.method == 'POST':
    form = MessageForm(request.POST)
    if form.is_valid():
      message = form.cleaned_data['message']
      Xtremefitness.objects.create(message=message)
      return render(request, 'template.html')
  else:
    form = MessageForm()
  return render(request, 'template.html', {'form': form})