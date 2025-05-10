from django.test import TestCase
from .models import Article, Category

class ArticleModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Local News')
        self.article = Article.objects.create(
            title='Test Article',
            content='This is a test article.',
            category=self.category
        )

    def test_article_creation(self):
        self.assertEqual(self.article.title, 'Test Article')
        self.assertEqual(self.article.content, 'This is a test article.')
        self.assertEqual(self.article.category.name, 'Local News')

    def test_article_str(self):
        self.assertEqual(str(self.article), 'Test Article')

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Local News')

    def test_category_creation(self):
        self.assertEqual(self.category.name, 'Local News')

    def test_category_str(self):
        self.assertEqual(str(self.category), 'Local News')