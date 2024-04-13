from django.db import models

class Departments(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self) -> str:
        return self.name
