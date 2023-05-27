from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter

from book import views

#router = SimpleRouter()
router = DefaultRouter()
router.register('authors', views.AuthorViewSet)
router.register('books', views.BookViewSet)

urlpatterns = router.urls

# urlpatterns = [
#     path('', include(router.urls))
    # path('library/authors/', views.list_authors, name='find_all_authors'),
    # path('library/authors/', views.AuthorView.as_view()),
    #path('author/<int:pk>/', views.AuthorDetailView.as_view()),
    # path('authors/<int:pk>', views.author_detail, name= 'author-detail'),
    # path('books/', views.list_books, name='find_all_books'),
    # path('book/<int:pk>', views.book_detail),
    # path('library/authors/', views.AuthorList.as_view()),
    # path('author/<int:pk>/', views.AuthorDetail.as_view()),
    # path('books/', views.BookList.as_view()),
    # path('book/<int:pk>/', views.BookDetail.as_view())

# ]
