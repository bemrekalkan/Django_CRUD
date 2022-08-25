from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

def index(request):
    return render(request, 'fscohort/index.html')


def student_list(request):
    students  = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'fscohort/student_list.html', context)

def student_add(request):
    form = StudentForm() # we will render blank form
    if request.method == 'POST':
        print(request.POST)
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
    context = {
        'form' : form
    }
    return render(request, 'fscohort/student_add.html', context)