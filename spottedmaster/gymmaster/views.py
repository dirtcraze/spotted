from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .forms import MessageForm
from .models import *

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())


def handle_form(request):
  form = MessageForm(request.POST or None)
  if request.method == "POST" and form.is_valid():
    message = form.cleaned_data["message"]
    if request.path == "/fitnessforlife/":
      Fitnessforlife.objects.create(message=message)
    elif request.path == "/fitnesstrzykorony/":
      Fitnesstrzykorony.objects.create(message=message)
    elif request.path == "/halnygym/":
      Halnygym.objects.create(message=message)
    elif request.path == "/oxygym/":
      Oxygym.objects.create(message=message)
    elif request.path == "/xtremefitness/":
      Xtremefitness.objects.create(message=message)
    return redirect("/")
  return render(request, "template.html", {"form": form})