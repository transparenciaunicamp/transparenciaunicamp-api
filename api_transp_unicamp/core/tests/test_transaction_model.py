from django.test import TestCase
from api_transp_unicamp.core.models import Category, Item, Transaction


class TestCreation(TestCase):

    def setUp(self):
        category = Category.objects.create(
            title='Parent',
            description='I am the parent'
        )
        credit = Item.objects.create(
            title='Whisky',
            description='Gotta love that',
            category=category,
            value=3.1415
        )
        debt = Item.objects.create(
            title='Sugar',
            description='Oh sugar sugar',
            category=category,
            value=-42
        )
        Transaction.objects.create(
            credit=credit,
            debt=debt
        )

    def test_create(self):
        self.assertEqual(1, Transaction.objects.count())
