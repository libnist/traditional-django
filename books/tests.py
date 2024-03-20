from django.test import TestCase
from django.urls import reverse

from books import models

# Create your tests here.
class BookTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = models.Book.objects.create(
            title="A good title",
            subtitle="An excellent subtitle",
            author="Tom Christie",
            isbn="1234567890123"
        )
        
    def test_book_content(self):
        self.assertEqual(self.book.title, "A good title")
        self.assertEqual(self.book.subtitle, "An excellent subtitle")
        self.assertEqual(self.book.author, "Tom Christie")
        self.assertEqual(self.book.isbn, "1234567890123")
        
    def test_book_list(self):
        response = self.client.get(reverse("books"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "excellent subtitle")
        self.assertTemplateUsed(response, "books/book_list.html")