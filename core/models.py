from django.db import models

from django.contrib.auth.models import User


class Habit(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=64)
    action = models.CharField(max_length=64)
    units = models.CharField(max_length=64, default='times')
    goal = models.PositiveIntegerField()
    owner = models.ForeignKey(
        User, related_name='habits', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField(blank=True, null=True)
    achievement = models.PositiveIntegerField(default=0)
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
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='observations', blank=True, null=True)
    habit = models.ForeignKey(
        Habit, on_delete=models.CASCADE, related_name='observers', blank=True, null=True)

    def __str__(self):
        return f"User: {self.user.pk} watches Habit: {self.habit.pk}"
