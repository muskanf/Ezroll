
from django.urls import path
from . import views

urlpatterns = [
    path('index', views.home, name="index" ),
    path('register', views.register, name="register" ),
    path('schedule', views.search_courses, name="schedule" ),
]
