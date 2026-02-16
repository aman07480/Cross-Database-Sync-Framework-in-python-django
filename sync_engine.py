from .models import Product

def sync_to_replica(product_instance):
    """
    Copy or update product into replica DB
    """

    Product.objects.using('replica').update_or_create(
        id=product_instance.id,
        defaults={
            "name": product_instance.name,
            "price": product_instance.price,
            "updated_at": product_instance.updated_at
        }
    )
