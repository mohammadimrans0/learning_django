from django.shortcuts import render, redirect
from learning_models.models import StudentModel
from learning_models.forms import StudentForm

# Create your views here.
def home(request):
    students = StudentModel.objects.all()
    return render(request, 'learning_models/home.html', {'studentData': students})

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/learning_models')
    else:
        form = StudentForm()
    return render(request, 'learning_models/create_student.html', {'form': form})


def delete_student(request, roll):
    student = StudentModel.objects.get(pk = roll).delete()
    return redirect("/learning_models")