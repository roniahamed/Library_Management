from django.urls import path 
from django.contrib.auth.decorators import login_required
from . import views
urlpatterns = [
    path('',views.Book_list.as_view(),name='show_book'),
    path('borrow/',views.Borrow_Book_list,name='borrow_book_list'),
    path('book_search/',views.Book_search.as_view(),name='book_search'),
    path('book_detail/<int:id>/',views.Book_details.as_view(),name='book_detail'),
    path('wishlist/',login_required(views.wishlist_show.as_view()), name='wishlist'),
    path('wishlist_create/<int:pk>/',views.add_wishlist, name='add_wishlist'),
    path('remove_wishlist/<int:pk>/',views.remove_wishlist, name='remove_wishlist'),
    path('borrowing/<int:pk>/',views.borrowing, name='borrow'),
    path('borrowing_return/<int:pk>/',views.borrowing_return, name='borrow_return'),
    path('add_book/',views.add_book, name='add_book'),
    path('delete_book/<int:pk>/',views.Book_Delete, name='book_delete'),
    path('edit_book/<int:pk>/',views.edit_book, name='edit_book'),
]
