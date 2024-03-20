from django.urls import path
from books import views

urlpatterns = [
    path("books", views.BookListView.as_view(), name="books")
]
