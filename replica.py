replica_product = Product.objects.using('replica').filter(id=product_instance.id).first()

if replica_product and replica_product.price != product_instance.price:
    print("Conflict detected")