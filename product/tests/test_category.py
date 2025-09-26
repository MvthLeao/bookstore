import pytest
from product.models import Category
from product.serializers.category_serializers import CategorySerializer

def test_category():
    category = Category.objects.create(
        title= 'produto3',
        slug= '003'
    )

    data = CategorySerializer(category).data

    assert data['title'] == 'produto3'
    assert data['slug'] == '003'