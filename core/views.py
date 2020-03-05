from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Habit, Record, Observer
from .forms import HabitForm, RecordForm


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


@login_required(login_url='/accounts/login/')
def add_habit(request):
    if request.method == "POST":
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.owner = request.user
            habit.save()
        return redirect('habits')
    else:
        form = HabitForm()
    return render(request, 'core/add_form.html', {'form': form, 'type': 'habit'})


@login_required(login_url='/accounts/login/')
def add_record(request):
    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.owner = request.user
            record.save()
            habit_pk = record.habit.pk
        return redirect('habit_records', habit_pk)
    else:
        form = RecordForm()
    return render(request, 'core/add_form.html', {'form': form, 'type': 'record'})
