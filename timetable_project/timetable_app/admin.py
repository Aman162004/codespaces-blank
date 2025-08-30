# timetable_app/admin.py
from django.contrib import admin
from .models import ClassRoom, Faculty, Course, Batch, TimeSlot, TimetableEntry

admin.site.register(ClassRoom)
admin.site.register(Faculty)
admin.site.register(Course)
admin.site.register(Batch)
admin.site.register(TimeSlot)
admin.site.register(TimetableEntry)