from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm

def index(request):
    persons = Person.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница', 'persons':persons})


def about(request):
    return render(request, 'main/about.html')


def registerUser(request):
    error = ''
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homePage')
        else:
            error = 'Неверрно введенные данные'
    form = PersonForm()
    context = {
        'form': form
    }
    return render(request, 'main/registration.html', context)
