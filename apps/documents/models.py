from django.db import models

class Documents(models.Model):
    description = models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.description
