# timetable_app/views.py
from django.shortcuts import render
from .models import TimetableEntry, Batch, Faculty

def home(request):
    return render(request, 'timetable_app/home.html')

def student_timetable(request):
    if request.method == 'POST':
        batch_id = request.POST.get('batch')
        batch = Batch.objects.get(id=batch_id)
        entries = TimetableEntry.objects.filter(batch=batch).order_by('time_slot__day', 'time_slot__start_time')
        context = {
            'entries': entries,
            'selected_batch': batch,
        }
        return render(request, 'timetable_app/student_timetable.html', context)
    
    batches = Batch.objects.all()
    context = {
        'batches': batches,
    }
    return render(request, 'timetable_app/student_timetable_form.html', context)

def faculty_timetable(request):
    if request.method == 'POST':
        faculty_id = request.POST.get('faculty')
        faculty = Faculty.objects.get(id=faculty_id)
        entries = TimetableEntry.objects.filter(faculty=faculty).order_by('time_slot__day', 'time_slot__start_time')
        context = {
            'entries': entries,
            'selected_faculty': faculty,
        }
        return render(request, 'timetable_app/faculty_timetable.html', context)

    faculties = Faculty.objects.all()
    context = {
        'faculties': faculties,
    }
    return render(request, 'timetable_app/faculty_timetable_form.html', context)