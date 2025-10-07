from django.test import TestCase
import pytest
from product.models import Category
from product.serializers.category_serializers import CategorySerializer

class TestCategorySerializer(TestCase):
    def test_category_serializer(self):
        category = Category.objects.create(
            title= 'produto3',
            slug= '003'
        )

        data = CategorySerializer(category).data

        assert data['title'] == 'produto3'
        assert data['slug'] == '003'
        