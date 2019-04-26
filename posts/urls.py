from django.urls import path
from . import views

app_name = "posts"
urlpatterns = [
    path('', views.StartView.as_view(), name="start"),
    path('create_post/', views.create_post, name='create_post'),
]