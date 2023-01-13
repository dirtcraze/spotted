from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .forms import MyForm
from .models import Fitnessforlife

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def fitnessforlife(request):
  if request.method == 'POST':
    form = MyForm(request.POST)
    if form.is_valid():
      input1 = form.cleaned_data['input1']
      return redirect('success_url')
  else:
    form = MyForm()
  return render(request, 'template.html', {'form': form}, context_instance=RequestContext(request))

def fitnesstrzykorony(request):
  template = loader.get_template('template.html')
  return HttpResponse(template.render())

def halnygym(request):
  template = loader.get_template('template.html')
  return HttpResponse(template.render())

def oxygym(request):
  template = loader.get_template('template.html')
  return HttpResponse(template.render())

def xtremefitness(request):
  template = loader.get_template('template.html')
  return HttpResponse(template.render())

def submit_view(request):
  if request.method == 'POST':
    input1 = request.POST['input1']
    Fitnessforlife.objects.create(message=input1)
    return redirect('success_url')
  else:
    return redirect('main_url')