from django.test import RequestFactory, TestCase
from django.urls import reverse

from .models import *

# title = models.CharField(max_length=100)
# description = models.TextField()
# author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
# genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
# language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
from .views import *


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        use = 12
        author = Author.objects.create(first_name="John", last_name="Wayne")
        language = Language.objects.create(name="Romanian")
        genres = [Genre.objects.create(name="drama")]
        cls.article = Article.objects.create(author=author, language=language,
                                         title='newArticle', description='newDescription')
        cls.article.genre.set(genres)

        cls.factory = RequestFactory()
        print(cls.article.genre.all())

    def test_articles_content(self):
        i = [i for i in Article.objects.all()]
        print(i)

    def test_author_last_name(self):
        author = Author.objects.get(pk=1)
        expected = f'{author.last_name}'
        self.assertEqual(expected, 'Wayne')

    def test_author_first_name(self):
        author = Author.objects.get(pk=1)
        expected = f'{author.first_name}'
        self.assertEqual(expected, 'John')

    def test_language_name(self):
        language = Language.objects.get(pk=1)
        expected = f'{language.name}'
        self.assertEqual(expected, 'Romanian')

    def test_language_verified(self):
        language = Language.objects.get(pk=1)
        expected = f'{language.name}'
        self.assertEqual(expected, 'Romanian')

    def test_article_content(self):
        self.assertEqual(f'{self.article.title}', 'newArticle')
        self.assertEqual(f'{self.article.author.last_name}', 'Wayne')
        self.assertEqual(f'{self.article.language.name}', 'Romanian')

    def test_articles_list_view(self):
        response = self.client.get(reverse('articles-list'))
        print(response)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'newDescription')

    def test_genre_list_view(self):
        response = self.client.get(reverse('genre-list'))
        print(response)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'drama')

    def test_author_list_view(self):
        response = self.client.get(reverse('author-list'))
        print(response)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Wayne')

    def test_articles_detail_view(self):
        response = self.client.get(reverse('articles-list'))
        no_response = self.client.get('/articles/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'newArticle')

    def test_author_detail_view(self):
        response = self.client.get(reverse('author-list'))
        no_response = self.client.get('/author/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'John')

    def test_genre_detail_view(self):
        response = self.client.get(reverse('genre-list'))
        no_response = self.client.get('/genre/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'drama')

    def test_post_update_view(self):
        response = self.client.post(reverse('articles-detail', args='1'), {
            'title': 'Updated title',
            'description': 'Updated text',
        })
        for post in Article.objects.all():
            print(f"---{post.pk}---")
        self.assertEqual(response.status_code, 405)

    #delete
    def test_delete_article_view(self):
        response = self.client.delete(reverse('articles-detail', args='1'))
        self.assertEqual(response.status_code, 204)



# Create your tests here.
