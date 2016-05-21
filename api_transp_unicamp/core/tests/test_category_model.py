from django.test import TestCase
from api_transp_unicamp.core.models import Category


class TestCreation(TestCase):

    def setUp(self):
        parent = Category.objects.create(
            title='Parent',
            description='I am the parent'
        )
        child = Category.objects.create(
            title='Child',
            description='I am the child',
            parent=parent
        )

    def test_create(self):
        self.assertEqual(2, Category.objects.count())
