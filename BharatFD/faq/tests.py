from django.test import TestCase
from faq.models import FAQ


class FAQTestCase(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question='What is the capital of India?',
            answer='Delhi',
            is_active=True
        )
