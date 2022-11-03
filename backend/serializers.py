from rest_framework import serializers
from .models import Todo
from datetime import date


class ToDoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = "__all__"
    
    def validate_deadline(self, value):
        if value < date.today():
            raise serializers.ValidationError('This field must be an even number.')
        return value