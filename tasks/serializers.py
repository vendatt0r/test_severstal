from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'status', 'created_at')
        read_only_fields = ('id', 'created_at')

    def validate_title(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError(
                "Название должно содержать минимум 3 символа"
            )
        return value
