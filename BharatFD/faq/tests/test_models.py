import pytest
from faq.models import FAQ


@pytest.mark.django_db
def test_faq_model():
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a Python framework.",
        is_active=True
    )
    assert str(faq) == "What is Django?"
    assert faq.is_active is True
    assert faq.answer == "Django is a Python framework."
