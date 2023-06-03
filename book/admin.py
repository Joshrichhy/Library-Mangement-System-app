from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from book.models import Author, Book, User


# Register your models here.
# how to customize your admin interface
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    list_filter = ['email']
    list_per_page = 10


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'genre']
    list_filter = ['title']
    list_per_page = 10


@admin.register(User)
class userAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "first_name", "last_name", "password1", "password2"),
            },
        ),
    )

