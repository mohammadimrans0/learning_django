from django.shortcuts import render
import datetime

def home(request):
    data = {
        'author': 'Paulo Coelho',
        'age': 77,
        'birthDay': datetime.datetime(1947, 8, 24),
        'bookList': ['The Alchemist','Brida','Veronika Decides to Die', 'Eleven Minutes'],
        'courses': [
            {'id': 1, 'name': 'python', 'fees': 500},
            {'id': 2, 'name': 'django', 'fees': 1500},
            {'id': 1, 'name': 'dbms', 'fees': 1000},
        ]
    }
    return render(request, 'navigation/home.html', data)

def about(request):
    return render(request, 'navigation/about.html')

def contact(request):
    return render(request, 'navigation/contact.html')
