from django.db import models

# Create your models here.


class Todo(models.Model):
    task = models.CharField(max_length=100)
    done = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.task.upper()} | {self.done}"