from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from .models import Todo
from .serializers import ToDoSerializer



class TODOViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for CRUD of TODO.
    """
    serializer_class = ToDoSerializer
    queryset = Todo.objects.all()
    filter_backends = [
      DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,
    ]
    filterset_fields = ("text", "complete", "deadline")
    search_fields = ("text", "deadline")
    ordering_fields = ("complete", "deadline")


  
