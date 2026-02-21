from django.urls import path
from .views import CreateProductView,ManualResyncView

urlpatterns = [
    path("create-product/", CreateProductView.as_view()),
    path("resync/<int:pk>/", ManualResyncView.as_view()),
]
