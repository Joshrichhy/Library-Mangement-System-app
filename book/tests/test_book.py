from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status


class TestBookEndPoint:
    def test_that_anonymous_user_cannot_get_book(self):
        client = APIClient()
        response = client.get('/library/books/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_that_anonymous_user_create_book(self):
        client = APIClient()
        response = client.post('/library/books/',
                                 {'title': 'my story', 'genre': 'LIT', 'isbn': '45654', 'price': 456, 'author': 56})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_that_admin_user_can_get_book(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.get('/library/books/')
        assert response.status_code == status.HTTP_200_OK

    def test_that_admin_get_400_with_wrong_book_info(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.post('/library/books/',
                               {'title': 'm', 'genre': 'C', 'isbn': '45654', 'price': 456, 'author': 56})
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_that_admin_get_201_with_right_book_info(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.post('/library/books/',
                               {'title': 'my story', 'genre': 'FIN', 'description': 'hello world', 'isbn': '45654', 'price': 456, 'author': 56})
        assert response.status_code == status.HTTP_201_CREATED