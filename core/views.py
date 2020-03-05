from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Habit, Record, Observer

# from .forms import ...


def home(request):
    return render(request, 'base.html')


@login_required(login_url='/accounts/login')
def habits(request):
    user = User.objects.get(username=request.user.username)
    habits = user.habits.all()
    context = {'habits': habits}
    return render(request, 'core/habits.html', context=context)


@login_required(login_url='/accounts/login')
def habit_records(request, pk):
    user = User.objects.get(username=request.user.username)
    habit = Habit.objects.get(pk=pk)
    records = Record.objects.filter(owner=user, habit=habit)
    context = {'records': records, 'habit': habit}
    return render(request, 'core/habit_records.html', context=context)
