from django.test import TestCase
from api.core.models import Category, Item


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
        Item.objects.create(
            title='Whisky',
            description='Gotta love that',
            category=child,
            value=3.1415
        )

    def test_create(self):
        self.assertEqual(1, Item.objects.count())
