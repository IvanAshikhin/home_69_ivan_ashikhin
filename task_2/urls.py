from django.urls import path
from task_2.views import calculate

urlpatterns = [
    path('task_2/calculate/', calculate, name='calculate'),
]
