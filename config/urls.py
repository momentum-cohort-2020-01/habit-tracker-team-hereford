from django.contrib import admin
from django.urls import include, path
from django.conf import settings

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),
    path('', views.habits, name='habits'),
    path('bar_chart/<int:pk>', views.bar_chart, name='bar_chart'),
    path('habit-records/<int:pk>', views.habit_records, name='habit_records'),
    path('add-habit/', views.add_habit, name='add_habit'),
    path('add-record/', views.add_record, name='add_record'),
    path('add-observer/<int:pk>', views.add_observer, name='add_observer'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns
