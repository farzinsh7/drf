from store.models import Collection
from model_bakery import baker
from rest_framework import status
import pytest


@pytest.fixture
def create_collection(api_client):
    def do_create_collection(collection):
        return api_client.post('/store/collections/', collection)
    return do_create_collection


@pytest.mark.django_db
class TestCreateCollection:
    def test_if_user_is_anonymous_returns_401(self, create_collection):
        response = create_collection({'title': 'a'})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self, authenticate, create_collection):
        authenticate()
        response = create_collection({'title': 'a'})

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_invalid_return_400(self, authenticate, create_collection):
        authenticate(is_staff=True)
        response = create_collection({'title': ''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None

    def test_if_data_is_valid_return_201(self, authenticate, create_collection):
        authenticate(is_staff=True)
        response = create_collection({'title': 'a'})

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0


@pytest.mark.django_db
class TestRetrieveCollection:
    def test_if_collection_exists_returns_200(self, api_client):
        collection = baker.make(Collection)
        response = api_client.get(f'/store/collections/{collection.id}/')

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id': collection.id,
            'title': collection.title,
            'products_count': 0,
        }

    def test_if_collection_does_not_exist_returns_404(self, api_client):
        response = api_client.get('/store/collections/999/')
        assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
class TestUpdateCollection:
    def test_if_user_is_anonymous_returns_401(self, api_client):
        collection = baker.make(Collection)
        response = api_client.patch(
            f'/store/collections/{collection.id}/', {'title': 'new title'})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self, authenticate, api_client):
        authenticate()
        collection = baker.make(Collection)
        response = api_client.patch(
            f'/store/collections/{collection.id}/', {'title': 'new title'})
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_user_is_admin_and_data_is_valid_returns_200(self, authenticate, api_client):
        authenticate(is_staff=True)
        collection = baker.make(Collection)
        response = api_client.patch(
            f'/store/collections/{collection.id}/', {'title': 'new title'})
        assert response.status_code == status.HTTP_200_OK
        assert response.data['title'] == 'new title'


@pytest.mark.django_db
class TestDeleteCollection:
    def test_if_user_is_anonymous_returns_401(self, api_client):
        collection = baker.make(Collection)
        response = api_client.delete(f'/store/collections/{collection.id}/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self, authenticate, api_client):
        authenticate()
        collection = baker.make(Collection)
        response = api_client.delete(f'/store/collections/{collection.id}/')
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_collection_has_associated_products_returns_405(self, authenticate, api_client):
        authenticate(is_staff=True)
        collection = baker.make(Collection)
        # Associate a product with the collection
        baker.make('store.Product', collection=collection)
        response = api_client.delete(f'/store/collections/{collection.id}/')
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        assert "Collection cannot deleted beacause it is associated with a product." in response.data[
            'Error']

    def test_if_collection_has_no_associated_products_returns_204(self, authenticate, api_client):
        authenticate(is_staff=True)
        collection = baker.make(Collection)
        response = api_client.delete(f'/store/collections/{collection.id}/')
        assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
class TestListCollections:
    def test_returns_all_collections(self, api_client):
        baker.make(Collection, _quantity=3)
        response = api_client.get('/store/collections/')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 3

    def test_products_count_in_collections(self, api_client):
        collection = baker.make(Collection)
        baker.make('store.Product', collection=collection, _quantity=2)
        response = api_client.get('/store/collections/')
        assert response.status_code == status.HTTP_200_OK
        assert response.data[0]['products_count'] == 2
