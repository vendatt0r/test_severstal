from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Task
from .serializers import TaskSerializer
from .filters import TaskFilter


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer

    queryset = Task.objects.all().order_by("-created_at")

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]

    filterset_class = TaskFilter

    ordering_fields = ["created_at", "title"]
    search_fields = ["title"]
