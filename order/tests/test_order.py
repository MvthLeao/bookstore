import pytest
from order.models import Order
from order.serializers.order_serializers import OrderSerializer
from product.models.product import Product
from product.models.category import Category
from django.contrib.auth.models import User

def test_order():
    user = User.objects.create(username='cliente1', email='cliente@client.com')

    product1 = Product.objects.create(
        title= 'produto1',
        description= '001',
        price='200',
        active=True
    )

    product2 = Product.objects.create(
        title= 'produto2',
        description= '002',
        price= '300',
        active=True
    )

    order = Order.objects.create(user=user)
    order.product.add(product1, product2)

    data = OrderSerializer(order).data

    assert data["total"] == 500
    assert len(data["product"]) == 2
