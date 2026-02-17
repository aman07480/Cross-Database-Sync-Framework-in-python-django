from django.urls import path
from .views import CreateProductView

urlpatterns = [
    path("create-product/", CreateProductView.as_view()),
]
