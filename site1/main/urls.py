from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="homePage"),
    path('about_us', views.about, name="aboutUsPage"),
    path('registration', views.registerUser, name="registerUserPage"),
]