from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product
from .sync_engine import sync_to_replica


@receiver(post_save, sender=Product)
def auto_sync_product(sender, instance, **kwargs):
    sync_to_replica(instance)
