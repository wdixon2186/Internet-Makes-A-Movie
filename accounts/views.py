from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

# class SignUp(generic.CreateView):
#    form_class = UserCreationForm
#    template_name = 'registration/signup.html'


def SignUp(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('script_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
