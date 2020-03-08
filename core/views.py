from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Habit, Record, Observer
from .forms import HabitForm, RecordForm, ObserverForm


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
        if not(get_date==-1 and get_habit_pk==-1):
            habit = Habit.objects.get(pk=get_habit_pk)
            form = RecordForm(initial={'habit': habit, 'date': get_date})
        else:
            form = RecordForm()
    return render(request, 'core/add_form.html', {'form': form, 'type': 'record'})


@login_required(login_url='/accounts/login/')
def habit_record(request, pk):
    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.owner = request.user
            record.save()
            habit_pk = record.habit.pk
        return redirect('habit_records', habit_pk)
    else:
        habit = Habit.objects.get(pk=pk)
        form = RecordForm(initial={'habit': habit})
    return render(request, 'core/add_form.html', {'form': form, 'type': 'record'})

@login_required(login_url='/accounts/login/')
def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'POST':
        form = HabitForm(request.POST, instance=habit)
        if form.is_valid():
            habit=form.save(commit=False)
            habit.owner = request.user
            habit.save()
        return redirect('habit_records', habit_pk)
    else:
        habit=Habit.objects.get(pk=pk)
        form = HabitForm(initial={'habit': habit})
    return render(request, 'core/edit_habit.html', {'form': form, 'type': 'habit'})

@login_required(login_url='/accounts/login/')
def edit_record(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == 'POST':
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            record=form.save(commit=False)
            record.owner = request.user
            record.save()
        return redirect('habit_records', habit_pk)
    else:
        record=Record.objects.get(pk=pk)
        form = RecordForm(initial={'type': 'record'})
    return render(request, 'core/edit_record.html', {'form': form, 'type': 'record'})

@login_required(login_url='/accounts/login/')
def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    habit.delete()
    return redirect('/')

@login_required(login_url='/accounts/login/')
def bar_chart(request, pk):
    labels = []
    data = []
    queryset = Habit.objects.order_by('-created_at')
    for habit in queryset:
        labels.append(habit.title)
        data.append(habit.units)

    return render(request, 'core/habit_records.html', {
        'labels': labels,
        'data': data,
    })

@login_required(login_url='/accounts/login/')
def add_observer(request, pk):
    if request.method == "POST":
        form = ObserverForm(request.POST)
        if form.is_valid():
            observer = form.save(commit=False)
            habit = Habit.objects.get(pk=pk)
            observer.habit = habit
            observer.save()
        return redirect('habit_records', pk)
    else:
        form = ObserverForm()
    return render(request, 'core/add_form.html', {'form': form})
