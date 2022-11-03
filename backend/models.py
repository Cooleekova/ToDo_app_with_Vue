from django.db import models

class Todo(models.Model):
    text = models.CharField(max_length=40)
    deadline = models.DateField()
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text