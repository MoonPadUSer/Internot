from django.urls import path
from . import views

from .forms import LoginForm
from django.views.generic.base import TemplateView

app_name = "users"
urlpatterns = [
    path('logout/', views.log_out, name="logout"),
    path('signup/', views.sign_up, name="signup"),
    path('profile/', TemplateView.as_view(template_name='profile.html')),
]