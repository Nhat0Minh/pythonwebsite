from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponseRedirect
from home.forms import RegistrationForm
from django.contrib.auth.models import User

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(
                form.cleaned_data['username'],
                form.cleaned_data['email'],
                form.cleaned_data['password1']
            )
            return HttpResponseRedirect('home')
    else:
        return render(request, 'pages/register.html', {'form': form})

def home(request):
    return render(request, 'pages/home.html')




