import pytest
from rest_framework.test import APIClient
from faq.models import FAQ


@pytest.mark.django_db
def test_faq_api(client):
    FAQ.objects.create(
        question="What is Django?",
        answer="Django is a Python web framework."
    )

    # Test the API endpoint for FAQs
    api_client = APIClient()
    response = api_client.get('/api/faqs/')

    # Assert the API response
    assert response.status_code == 200
    assert response.data[0]['question'] == "What is Django?"
    assert response.data[0]['answer'] == "Django is a Python web framework."
