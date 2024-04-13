from django.db import models

class Companies(models.Model):
    name = models.CharField(max_length=100, help_text='Nome da empresa')

    def __str__(self) -> str:
        return self.name
    


