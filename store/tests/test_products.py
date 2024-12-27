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


# @pytest.mark.django_db
# class TestUpdateCollection:
#     def test_if_user_is_anonymous_returns_401(self, api_client):
#         collection = baker.make(Collection)
#         response = api_client.patch(
#             f'/store/collections/{collection.id}/', {'title': 'new title'})
#         assert response.status_code == status.HTTP_401_UNAUTHORIZED

#     def test_if_user_is_not_admin_returns_403(self, authenticate, api_client):
#         authenticate()
#         collection = baker.make(Collection)
#         response = api_client.patch(
#             f'/store/collections/{collection.id}/', {'title': 'new title'})
#         assert response.status_code == status.HTTP_403_FORBIDDEN

#     def test_if_user_is_admin_and_data_is_valid_returns_200(self, authenticate, api_client):
#         authenticate(is_staff=True)
#         collection = baker.make(Collection)
#         response = api_client.patch(
#             f'/store/collections/{collection.id}/', {'title': 'new title'})
#         assert response.status_code == status.HTTP_200_OK
#         assert response.data['title'] == 'new title'


# @pytest.mark.django_db
# class TestDeleteCollection:
#     def test_if_user_is_anonymous_returns_401(self, api_client):
#         collection = baker.make(Collection)
#         response = api_client.delete(f'/store/collections/{collection.id}/')
#         assert response.status_code == status.HTTP_401_UNAUTHORIZED

#     def test_if_user_is_not_admin_returns_403(self, authenticate, api_client):
#         authenticate()
#         collection = baker.make(Collection)
#         response = api_client.delete(f'/store/collections/{collection.id}/')
#         assert response.status_code == status.HTTP_403_FORBIDDEN

#     def test_if_collection_has_associated_products_returns_405(self, authenticate, api_client):
#         authenticate(is_staff=True)
#         collection = baker.make(Collection)
#         # Associate a product with the collection
#         baker.make('store.Product', collection=collection)
#         response = api_client.delete(f'/store/collections/{collection.id}/')
#         assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
#         assert "Collection cannot deleted beacause it is associated with a product." in response.data[
#             'Error']

#     def test_if_collection_has_no_associated_products_returns_204(self, authenticate, api_client):
#         authenticate(is_staff=True)
#         collection = baker.make(Collection)
#         response = api_client.delete(f'/store/collections/{collection.id}/')
#         assert response.status_code == status.HTTP_204_NO_CONTENT


# @pytest.mark.django_db
# class TestListCollections:
#     def test_returns_all_collections(self, api_client):
#         baker.make(Collection, _quantity=3)
#         response = api_client.get('/store/collections/')
#         assert response.status_code == status.HTTP_200_OK
#         assert len(response.data) == 3

#     def test_products_count_in_collections(self, api_client):
#         collection = baker.make(Collection)
#         baker.make('store.Product', collection=collection, _quantity=2)
#         response = api_client.get('/store/collections/')
#         assert response.status_code == status.HTTP_200_OK
#         assert response.data[0]['products_count'] == 2
