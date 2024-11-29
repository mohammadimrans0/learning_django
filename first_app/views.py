from django.shortcuts import render
from .forms import DjangoForm, StudentForm, PasswordValidator

def home(request): 
    return render(request, 'first_app/home.html')

def form(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('useremail')
        select = request.POST.get('select')
        return render(request, 'first_app/form.html',
                       {
                         'name': name,
                         'email': email,
                         'select': select
                       }
                    )
    
    return render(request, 'first_app/form.html')

def djangoForm(request):
    if request.method == 'POST':
        form = DjangoForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']

            with open('first_app/upload/' + file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

            print(form.cleaned_data)
            return render(request, 'first_app/django_form.html', {'form': form})
    else:
        form = DjangoForm()

    return render(request, 'first_app/django_form.html', {'form': form})


def studentForm(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request, 'first_app/student_form.html', {'form': form})
    else:
        form = StudentForm()

    return render(request, 'first_app/student_form.html', {'form': form})

def passwordValidator(request):
    if request.method == 'POST':
        form = PasswordValidator(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request, 'first_app/password_validator.html', {'form': form})
    else:
        form = PasswordValidator()

    return render(request, 'first_app/password_validator.html', {'form': form})