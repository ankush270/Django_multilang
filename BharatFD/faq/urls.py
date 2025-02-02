from django.urls import path
from . import views

app_name = 'faq'

urlpatterns = [
    path('', views.faq_list, name='faq_list'),
    path('create/', views.create_faq, name='create_faq'),
    path('api/faqs/', views.FAQListAPIView.as_view(), name='faq_api_list'),
]
