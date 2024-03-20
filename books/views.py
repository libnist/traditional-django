from django.shortcuts import render
from django.views.generic import ListView

from books import models

# Create your views here.
class BookListView(ListView):
    model = models.Book
    template_name = "book_list.html"