from django.urls import path
from .views import TaskCreateView

urlpatterns = [
    path('add/', TaskCreateView.as_view(), name='task-add'),
]
