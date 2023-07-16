from django.contrib import admin

from management.models import Book,Wishlist, Borrowing

# Register your models here.
admin.site.register(Book)
admin.site.register(Wishlist)
admin.site.register(Borrowing)