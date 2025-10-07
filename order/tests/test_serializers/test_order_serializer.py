from django.test import TestCase
from django.contrib.auth.models import User
from product.models import Product
from order.models import Order
from order.serializers.order_serializers import OrderSerializer


class TestOrderSerializer(TestCase):
    def test_order_serializer(self):
        user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )

        product1 = Product.objects.create(
            title="Produto 1",
            description="Descrição do Produto 1",
            price=100,
            active=True
        )
        product2 = Product.objects.create(
            title="Produto 2",
            description="Descrição do Produto 2",
            price=200,
            active=True
        )

        data = {
            "products_id": [product1.id, product2.id],
            "user": user.id,
        }

        serializer = OrderSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)

        order = serializer.save()
        serialized_order = OrderSerializer(order).data

        self.assertEqual(serialized_order["total"], 300)
        self.assertEqual(serialized_order["user"], user.id)
