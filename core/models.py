from datetime import date
from django.db import models

from django.contrib.auth.models import User


class Habit(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(
        max_length=64, help_text='The name of your new habit')
    action = models.CharField(
        max_length=64, help_text='What action are you performing for this habit?')
    units = models.CharField(max_length=64, default='times',
                             help_text='The units/how many times you want to do your habit daily')
    goal = models.PositiveIntegerField(
        help_text='How much you want accomplish daily')
    owner = models.ForeignKey(
        User, related_name='habits', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField(default=date.today, )
    achievement = models.PositiveIntegerField(
        default=0, help_text='How much/many times do you do your habit?')
    habit = models.ForeignKey(
        Habit, on_delete=models.CASCADE, related_name='records', blank=True, null=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='records', blank=True, null=True)

    def __str__(self):
        return f"{self.owner.username}'s {self.habit.title} on {self.date}"

    class Meta:
        ordering = ['-date']
        constraints = [models.UniqueConstraint(
            fields=['date', 'habit', 'owner'], name='unique_record')]


class Observer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    observer = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='observations', blank=True, null=True)
    habit = models.ForeignKey(
        Habit, on_delete=models.CASCADE, related_name='observers', blank=True, null=True)

    def __str__(self):
        return f"User: {self.user.pk} watches Habit: {self.habit.pk}"
