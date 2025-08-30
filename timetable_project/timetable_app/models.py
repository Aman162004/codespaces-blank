# timetable_app/models.py
from django.db import models

class ClassRoom(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.IntegerField()
    is_lab = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.code} - {self.name}"

class Batch(models.Model):
    YEAR_CHOICES = [
        ('1st', '1st Year'),
        ('2nd', '2nd Year'),
        ('3rd', '3rd Year'),
    ]
    STREAM_CHOICES = [
        ('CSE', 'CSE'),
        ('ECE', 'ECE'),
        ('EE', 'EE'),
    ]
    SECTION_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('N/A', 'Not Applicable'),
    ]

    year = models.CharField(max_length=10, choices=YEAR_CHOICES)
    stream = models.CharField(max_length=10, choices=STREAM_CHOICES)
    section = models.CharField(max_length=10, choices=SECTION_CHOICES, default='N/A')
    students_count = models.IntegerField()

    def __str__(self):
        return f"{self.year} Year, {self.stream} {self.section}"

class TimeSlot(models.Model):
    DAY_CHOICES = [
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
    ]
    day = models.CharField(max_length=3, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        unique_together = ('day', 'start_time')
        ordering = ['day', 'start_time']

    def __str__(self):
        return f"{self.get_day_display()} {self.start_time.strftime('%H:%M')} - {self.end_time.strftime('%H:%M')}"

class TimetableEntry(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    is_lab = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.course.code} at {self.time_slot} for {self.batch}"