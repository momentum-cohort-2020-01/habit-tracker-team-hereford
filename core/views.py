from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Habit, Record, Observer

# from .forms import ...

def home(request):
  return render(request, 'base.html')