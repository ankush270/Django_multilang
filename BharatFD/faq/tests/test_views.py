import pytest
from django.urls import reverse
from faq.models import FAQ


@pytest.mark.django_db
def test_faq_list_view(client):
    FAQ.objects.create(question="Test?", answer="Test Answer.")
    url = reverse("faq:faq_list")  
    response = client.get(url)
    assert response.status_code == 200
    assert "Test?" in response.content.decode()
