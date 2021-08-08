from django.urls import path

from . import views
#all pattern
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('book_list/', views.BookListView.as_view(), name='BookListView'),
    path('book/<pk>', views.BookDetailView.as_view(), name='book-detail'),
        path('book/create/', views.BookCreate.as_view(), name='book_create'),
    path('author/<pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('author_list/', views.AuthorListView.as_view(), name='AuthorListView'),
    path('book/<pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]
urlpatterns += [
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]
urlpatterns += [
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]
