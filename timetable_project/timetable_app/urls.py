# timetable_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('student/', views.student_timetable, name='student_timetable'),
    path('faculty/', views.faculty_timetable, name='faculty_timetable'),
]