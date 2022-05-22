from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
        return render(request, 'registration/register.html', {'form': form})

    else:
        form = UserCreationForm()
        return render(request, 'registration/register.html', {'form': form})
