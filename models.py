from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    sync_status = models.CharField(max_length=20, default="pending")

    def __str__(self):
        return self.name
