from django.test import TestCase
from api.core.models import Institute


class TestCreation(TestCase):

    def setUp(self):
        parent = Institute.objects.create(
            title='Parent',
            description='I am the parent'
        )
        Institute.objects.create(
            title='Child',
            description='I am the child',
            parent=parent
        )

    def test_create(self):
        self.assertEqual(2, Institute.objects.count())
