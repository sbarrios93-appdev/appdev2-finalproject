from django.db import models

# Create your models here.


class Sport(models.Model):
    name = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def normalized_name(self):
        return self.name.lower()

    def __str__(self):
        return self.name
