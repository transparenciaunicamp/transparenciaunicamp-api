from django.test import TestCase
from api_transp_unicamp.core.models import Institute, Category, Document


class TestCreation(TestCase):

    def setUp(self):
        category = Category.objects.create(
            title='Category',
            description='I am the category'
        )
        institute = Institute.objects.create(
            title='Institute',
            description='I am  the institute'
        )
        Document.objects.create(
            title='DRE',
            description='D.R.E.',
            category=category,
            institute=institute,
            month=12,
            year=2014
        )

    def test_create(self):
        self.assertEqual(1, Document.objects.count())
