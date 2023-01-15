from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.urls import resolve
from .forms import MessageForm

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def handle_form(request):
  form = MessageForm(request.POST or None)
  if request.method == "POST" and form.is_valid():
    message = form.cleaned_data["message"]
    ip = request.META['REMOTE_ADDR']
    device = request.META.get('HTTP_USER_AGENT')
    view_name = resolve(request.path_info).url_name
    if view_name == "fitnessforlife":
      Fitnessforlife.objects.create(message=message, user_ip=ip, device=device)
    elif view_name == "fitnesstrzykorony":
      Fitnesstrzykorony.objects.create(message=message, user_ip=ip, device=device)
    elif view_name == "halnygym":
      Halnygym.objects.create(message=message, user_ip=ip, device=device)
    elif view_name == "oxygym":
      Oxygym.objects.create(message=message, user_ip=ip, device=device)
    elif view_name == "xtremefitness":
      Xtremefitness.objects.create(message=message, user_ip=ip, device=device)
    
    # return redirect("/")
  return render(request, "template.html", {"form": form})