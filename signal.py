# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Product
# from .sync_engine import sync_to_replica


# @receiver(post_save, sender=Product)
# def auto_sync_product(sender, instance, **kwargs):
#     sync_to_replica(instance)

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Product
from .sync_engine import sync_to_replica


@receiver(post_save, sender=Product)
def auto_sync_product(sender, instance, **kwargs):
    sync_to_replica(instance)


@receiver(post_delete, sender=Product)
def auto_delete_replica(sender, instance, **kwargs):
    Product.objects.using('replica').filter(id=instance.id).delete()