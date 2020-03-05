from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Habit, Record, Observer

# from .forms import ...

def home(request):
  return render(request, 'base.html')

@login_required(login_url='/accounts/login')
def habits(request):
  user= User.objects.get(username=request.user.username)
  habits= user.habits.all()
  context={'habits': habits}
  return render(request, 'core/habits.html', context=context)

def user_record(request):
  user= User.objects.get(username=request.user.username) 
  context={}
  return render(requerst, 'core/record.html', context=context)