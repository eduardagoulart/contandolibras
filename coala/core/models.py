from django.db import models


class SubscriptionsModels(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=100, null=True, blank=True)
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.name