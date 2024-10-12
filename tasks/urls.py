from django.urls import path
from .views import TaskCreateView, TaskUpdateView, UserTaskListView

urlpatterns = [
    path('add/', TaskCreateView.as_view(), name='task-add'),
    path('<int:pk>/', TaskUpdateView.as_view(), name='update-task'),
    path('my-tasks/', UserTaskListView.as_view(), name='task-list'),
]
