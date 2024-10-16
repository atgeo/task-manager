from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'is_completed', 'priority', 'user']
