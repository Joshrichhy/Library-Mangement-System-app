from django.core.mail import send_mail, BadHeaderError, EmailMessage
from rest_framework.decorators import api_view
# to send html mail
from templated_mail.mail import BaseEmailMessage
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAdminUser, DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from book.models import Author, Book
from .filter import AuthorFilter, BookFilter
from .permissions import IsAdminOrReadOnly
from .serializers import AuthorSerializer, BookSerializer
from .pagination import DefaultPagination, DefaultBookPagination


# Create your views here.
class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = AuthorFilter
    search_fields = ['name', 'date_of_birth']
    permission_classes = [IsAdminOrReadOnly]
    # or permission_classes = [IsAuthenticated]
    # or permission_classes = [DjangoModelPermissions]


class BookViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = DefaultBookPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = BookFilter
    search_fields = ['title', 'price']
    #permission_classes = [DjangoModelPermissions]


# class AuthorList(ListCreateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
# or
# def get_queryset(self):
#     return Author.objects.all()
#
# def get_serializer_class(self):
#     return AuthorSerializer


# class AuthorDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer


# class BookList(ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#     def get_serializer_context(self):
#         return {"request": self.request}
#
#
# class BookDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class AuthorView(APIView):
#     def get(self, request):
#         authors = Author.objects.all()
#         serializer = AuthorSerializer(authors, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         serialize = AuthorSerializer(data=request.data)
#         serialize.is_valid(raise_exception=True)
#         serialize.save()
#         return Response("Successful", status=status.HTTP_201_CREATED)
#
#
# class AuthorDetailView(APIView):
#     def get(self, request, pk):
#         author = get_object_or_404(Author, pk=pk)
#         serializer = AuthorSerializer(author)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, pk):
#         author = get_object_or_404(Author, pk=pk)
#         serializer = AuthorSerializer(author, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response("detail Updated", status=status.HTTP_200_OK)
#
#     def delete(self, request, pk):
#         author = get_object_or_404(Author, pk=pk)
#         author.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# def list_authors(request):
#     if request.method == 'GET':
#         authors = Author.objects.all()
#         serializer = AuthorSerializer(authors, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serialize = AuthorSerializer(data=request.data)
#         serialize.is_valid(raise_exception=True)
#         serialize.save()
#         return Response("Successful", status=status.HTTP_201_CREATED)


# @api_view(['GET', 'PUT', 'DELETE'])
# def author_detail(request, pk):
#     author = get_object_or_404(Author, pk=pk)
#     if request.method == 'GET':
#         serializer = AuthorSerializer(author)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == 'PUT':
#         serializer = AuthorSerializer(author, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response("detail Updated", status=status.HTTP_200_OK)
#
#     elif request.method == 'DELETE':
#         author.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'DELETE', 'PUT'])
# def book_detail(request, pk):
#     book = Book.objects.get(pk=pk)
#     if request.method == 'GET':
#         serializer = BookSerializer(book)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = BookSerializer(Book, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response("Book detail Updated", status=status.HTTP_200_OK)
#
#
# @api_view(['GET', 'POST'])
# def list_books(request):
#     books = Book.objects.all()
#     serializer = BookSerializer(books, many=True, context={'request': request})
#     return Response(serializer.data, status=status.HTTP_200_OK)

def send_mail_function(request):
    # send_mass_mail for sending mail  to more than one person
    try:
        send_mail("Library message", "your book is now available", "kkj@gmail.com", ["kusejoshua@gmail.com"])
    except BadHeaderError:
        pass
    return HttpResponse('message sent')


def email_function(request):
    try:
        message = EmailMessage("Library message", "your book is now available", "kkj@gmail.com",
                               ["kusejoshua@gmail.com"])
        message.attach_file('book\\static\\images\\R.jfif')
        message.send()
    except BadHeaderError:
        pass
    return HttpResponse('message sent')

@api_view(['GET'])
def templatemail_function(request):
    try:
        message = BaseEmailMessage(template_name='book/email.html', context={'name': 'Joshrichhy'} )
        message.send(['kusejoshua@gmail.com'])
    except BadHeaderError:
        pass
    return HttpResponse('message sent successfully')
