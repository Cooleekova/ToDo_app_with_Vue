from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from .models import Todo
from .serializers import ToDoSerializer



class TODOViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for CRUD of TODO.
    """

    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer
    filter_backends = [
      DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,
    ]
    filterset_fields = ("text", "complete")
    search_fields = ("text")
    ordering_fields = ("complete",)
