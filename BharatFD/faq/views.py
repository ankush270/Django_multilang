from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from .models import FAQ
from googletrans import Translator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import concurrent.futures  # To perform parallel translations


# Initialize the Google Translator
translator = Translator()


# Function to translate text to a given language
class FAQListAPIView(APIView):
    def get(self, request):
        faqs = FAQ.objects.filter(is_active=True)
        data = [
            {'question': faq.question, 'answer': faq.answer}
            for faq in faqs
        ]
        return Response(data, status=status.HTTP_200_OK)


def translate_text(text, lang):
    return translator.translate(text, dest=lang).text


# View to display FAQ list
def faq_list(request):
    # Get language from request (default to 'en' if not specified)
    language = request.GET.get('lang', 'en')
    # Get all active FAQs
    faqs = FAQ.objects.filter(is_active=True)

    # Prepare translated FAQs
    translated_faqs = [
        {
            'question': faq.get_question(language),
            'answer': faq.get_answer(language)
        }
        for faq in faqs
    ]
    return render(request, 'faq/faq_list.html', {
        'faqs': translated_faqs,
        'current_language': language
    })


@staff_member_required
def create_faq(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        answer = request.POST.get('answer')

        # Languages to translate into
        languages = ["hi", "bn", "gu", "ta", "te", "kn"]

        translated_data = {"question": question, "answer": answer}
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = {
                executor.submit(translate_text, question, lang):
                f"question_{lang}" for lang in languages
            }
            futures.update({
                executor.submit(translate_text, answer, lang): f"answer_{lang}"
                for lang in languages
            })
            for future in concurrent.futures.as_completed(futures):
                lang_field = futures[future]
                translated_data[lang_field] = future.result()

        # Create the FAQ instance with translated data
        FAQ.objects.create(
            question=translated_data["question"],
            answer=translated_data["answer"],
            question_hi=translated_data["question_hi"],
            answer_hi=translated_data["answer_hi"],
            question_bn=translated_data["question_bn"],
            answer_bn=translated_data["answer_bn"],
            question_gu=translated_data["question_gu"],
            answer_gu=translated_data["answer_gu"],
            question_ta=translated_data["question_ta"],
            answer_ta=translated_data["answer_ta"],
            question_te=translated_data["question_te"],
            answer_te=translated_data["answer_te"],
            question_kn=translated_data["question_kn"],
            answer_kn=translated_data["answer_kn"],
            is_active=True
        )

        messages.success(request, 'FAQ created successfully!')
        return redirect('faq:faq_list')

    return render(request, 'faq/create_faq.html')
