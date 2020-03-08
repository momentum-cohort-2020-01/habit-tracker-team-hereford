from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Habit, Record, Observer
from .forms import HabitForm, RecordForm, ObserverForm


@login_required(login_url='/accounts/login')
def habits(request):
    user = User.objects.get(username=request.user.username)
    habits = user.habits.all()
    observations = user.observations.all()
    context = {'habits': habits, 'observations': observations}
    return render(request, 'core/habits.html', context=context)


@login_required(login_url='/accounts/login')
def habit_records(request, pk):
    user = User.objects.get(username=request.user.username)
    habit = Habit.objects.get(pk=pk)
    owner = habit.owner
    records = Record.objects.filter(owner=owner, habit=habit)
    observers = habit.observers.all()
    observers_usernames = [obs.observer.username for obs in observers]
    context = {'records': records, 'habit': habit,
               'observers': observers_usernames}
    if user == owner:
        return render(request, 'core/habit_records.html', context=context)
    else:
        return render(request, 'core/habit_records_observer.html', context=context)


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
    context = {'form': form, 'type': 'habit'}
    return render(request, 'core/add_form.html', context=context)


@login_required(login_url='/accounts/login/')
def add_record(request):
    user = User.objects.get(username=request.user.username)
    get_habit_pk = request.GET.get('habit', -1)
    get_date = request.GET.get('date', -1)
    if request.method == "POST":
        user = request.user
        habit = Habit.objects.get(pk=request.POST['habit'])
        form = RecordForm(request.POST)
        if form.is_valid():
            if Record.objects.filter(owner=user, date=request.POST['date'], habit=habit):
                form = RecordForm()
                context = {'form': form, 'type': 'record', 'warning': True}
                return render(request, 'core/add_form.html', context=context)
            else:
                record = form.save(commit=False)
                record.owner = user
                record.save()
                habit_pk = record.habit.pk
                return redirect('habit_records', habit_pk)
    else:
        if not(get_date == -1 and get_habit_pk == -1):
            habit = Habit.objects.get(pk=get_habit_pk)
            form = RecordForm()
            form.fields['habit'].queryset = user.habits
            form.initial = {'habit': habit, 'date': get_date}
        else:
            form = RecordForm()
            form.fields['habit'].queryset = user.habits
    context = {'form': form, 'type': 'record'}
    return render(request, 'core/add_form.html', context=context)


@login_required(login_url='/accounts/login/')
def edit_habit(request, pk):
    user = User.objects.get(username=request.user.username)
    habit = get_object_or_404(Habit, pk=pk)
    if habit.owner != user:
        return redirect('/')
    if request.method == 'POST':
        form = HabitForm(request.POST, instance=habit)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.owner = request.user
            habit.save()
        return redirect('habit_records', pk)
    else:
        habit = Habit.objects.get(pk=pk)
        form = HabitForm(instance=habit)
    context = {'form': form, 'type': 'habit'}
    return render(request, 'core/edit_habit.html', context=context)


@login_required(login_url='/accounts/login/')
def edit_record(request):
    habit_pk = request.GET.get('habit', -1)
    date = request.GET.get('date', -1)
    user = User.objects.get(username=request.user.username)
    habit = get_object_or_404(Habit, pk=habit_pk)
    if habit.owner != user:
        return redirect('/')
    record = get_object_or_404(Record, habit=habit, date=date)
    if request.method == 'POST':
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            record = form.save(commit=False)
            record.owner = request.user
            record.save()
        return redirect('habit_records', pk)
    else:
        # record = Record.objects.get(pk=pk)
        form = RecordForm(
            initial={'habit': habit, 'date': date, 'achievement': record.achievement})
        form.fields['habit'].queryset = user.habits
    context = {'form': form, 'type': 'record'}
    return render(request, 'core/edit_record.html', context=context)


@login_required(login_url='/accounts/login/')
def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    user = User.objects.get(username=request.user.username)
    if habit.owner != user:
        return redirect('/')
    habit.delete()
    return redirect('/')


@login_required(login_url='/accounts/login/')
def add_observer(request, pk):
    user = User.objects.get(username=request.user.username)
    if request.method == "POST":
        form = ObserverForm(request.POST)
        if form.is_valid():
            habit = Habit.objects.get(pk=pk)
            if habit.owner != user:
                return redirect('/')
            if Observer.objects.filter(observer=User.objects.get(pk=request.POST['observer']), habit=habit):
                form = ObserverForm()
                context = {'form': form, 'type': 'observer', 'warning': True}
                return render(request, 'core/add_form.html', context=context)
            else:
                observer = form.save(commit=False)
                observer.habit = habit
                observer.save()
                return redirect('habit_records', pk)
        return redirect('habit_records', pk)
    else:
        form = ObserverForm()
    return render(request, 'core/add_form.html', {'form': form})
