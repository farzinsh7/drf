from store.models import Product
from model_bakery import baker
from rest_framework import status
import pytest


@pytest.fixture
def create_product(api_client):
    def do_create_product(product):
        return api_client.post('/store/products/', product)
    return do_create_product


@pytest.fixture
def product_payload():
    def create_payload(**overrides):
        collection = baker.make('store.Collection')  # Create a collection
        payload = {
            'title': 'a',
            'slug': 'a',
            'description': 'a',
            'unit_price': 1,
            'inventory': 10,
            'collection': collection.id
        }
        payload.update(overrides)  # Allow customization of payload
        return payload
    return create_payload


@pytest.mark.django_db
class TestCreateProduct:
    def test_if_user_is_anonymous_returns_401(self, create_product, product_payload):
        response = create_product(product_payload())
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self, authenticate, create_product, product_payload):
        authenticate()
        response = create_product(product_payload())
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_invalid_returns_400(self, authenticate, create_product, product_payload):
        authenticate(is_staff=True)
        invalid_payload = product_payload(
            title='', slug='', unit_price=0, inventory=-1)
        response = create_product(invalid_payload)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'title' in response.data
        assert 'unit_price' in response.data
        assert 'inventory' in response.data

    def test_if_data_is_valid_returns_201(self, authenticate, create_product, product_payload):
        authenticate(is_staff=True)
        response = create_product(product_payload())
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0


@pytest.mark.django_db
class TestRetrieveProduct:
    def test_if_product_does_not_exist_returns_404(self, api_client):
        response = api_client.get('/store/products/999/')
        assert response.status_code == status.HTTP_404_NOT_FOUND
