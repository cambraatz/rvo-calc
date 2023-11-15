from django.urls import path
from portfolio import views

urlpatterns = [
    path("", views.home, name="home"),
    path("portfolio/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]