from django.urls import path

from task_2.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
