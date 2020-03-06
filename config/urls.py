from django.contrib import admin
from django.urls import include, path
from django.conf import settings

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),
    path('', views.habits, name='habits'),
    path('habit-records/<int:pk>', views.habit_records, name='habit_records'),
    path('add-habit/', views.add_habit, name='add_habit'),
    path('add-record/', views.add_record, name='add_record'),
    path('add-habit-record/<int:pk>', views.habit_record, name='add_habit_record'),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns
