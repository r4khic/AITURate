from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name="main"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('subjects', views.disciplines, name="disciplines"),
    path('teachers', views.teachers, name="teachers"),
    path('teacher', views.teacher, name="teacher"),
    path('rating', views.rating, name="rating"),
]
