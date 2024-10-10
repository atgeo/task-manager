from django.urls import path
from .views import TaskCreateView, UserTaskListView

urlpatterns = [
    path('add/', TaskCreateView.as_view(), name='task-add'),
    path('my-tasks/', UserTaskListView.as_view(), name='task-list'),
]
