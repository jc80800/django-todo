# todo_app/urls.py
from django.urls import path
from . import views
from .views import TaskCreate

urlpatterns = [
    path("", views.index, name='tasks'),
    path('create-task/', TaskCreate.as_view(), name='create-task')
]
