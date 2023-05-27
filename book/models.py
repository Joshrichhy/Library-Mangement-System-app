from uuid import uuid4

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)


class Author(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    date_of_death = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}  "


class Book(models.Model):
    LANGUAGE_CHOICES = [
        ("Y", "YORUBA"),
        ("E", "ENGLISH"),
        ("H", "HAUSA"),
        ("I", "IGBO")
    ]

    GENRE_CHOICES = [
        ('FIC', 'FICTION'),
        ('POL', 'POLITICS'),
        ('FIN', 'FINANCE'),
        ('ROM', 'ROMANCE')
    ]

    title = models.CharField(max_length=255, blank=False, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=False, null=False)
    date_added = models.DateTimeField(blank=True, null=True)
    isbn = models.CharField(max_length=13, blank=False, null=False)
    genre = models.CharField(choices=GENRE_CHOICES, max_length=15)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    language = models.CharField(max_length=15, choices=LANGUAGE_CHOICES)

    def __str__(self):
        return f"{self.title} {self.author.name} {self.description} {self.isbn}" \
               f"{self.genre} {self.language}"


class BookInstance(models.Model):
    STATUS_CHOICES = [
        ('AVAILABLE', 'A'),
        ('BORROWED', 'B'),

    ]

    unique_id = models.UUIDField(primary_key=True, default=uuid4)
    due_back = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='A')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.due_back} {self.status} {self.book} "
