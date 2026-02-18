from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product


class CreateProductView(APIView):

    def post(self, request):
        name = request.data.get("name")
        price = request.data.get("price")

        product = Product.objects.create(
            name=name,
            price=price
        )

        return Response({
            "msg": "Product created & synced",
            "id": product.id
            "no":product.no
        })
