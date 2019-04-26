from django.urls import reverse_lazy, reverse
from django.views import generic

from .forms import CustomUserCreationForm

from django.http import request, HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from django.contrib.auth import logout

"""
class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
"""

def log_out(request):
    logout(request)
    return render(request, 'registration/logged_out.html')

def sign_up(request):
    if request.POST:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        return HttpResponse((username, email, password))
    else:
        return render(request, 'signup.html')
