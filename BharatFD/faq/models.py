from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from django.core.cache import cache
from googletrans import Translator
from django.utils import timezone


translator = Translator()


class FAQ(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    question = models.TextField(verbose_name=_('Question'))
    answer = RichTextField(verbose_name=_('Answer'))

    # Translations
    LANGUAGE_CHOICES = {
        "hi": "Hindi",
        "bn": "Bengali",
        "gu": "Gujarati",
        "ta": "Tamil",
        "te": "Telugu",
        "kn": "Kannada",
    }

    # Define translation fields
    question_hi = models.TextField(
        verbose_name=_("Question (Hindi)"),
        blank=True)
    answer_hi = RichTextField(verbose_name=_("Answer (Hindi)"), blank=True)

    question_bn = models.TextField(
        verbose_name=_("Question (Bengali)"),
        blank=True)
    answer_bn = RichTextField(verbose_name=_("Answer (Bengali)"), blank=True)

    question_gu = models.TextField(
        verbose_name=_("Question (Gujarati)"),
        blank=True)
    answer_gu = RichTextField(verbose_name=_("Answer (Gujarati)"), blank=True)

    question_ta = models.TextField(
        verbose_name=_("Question (Tamil)"),
        blank=True)
    answer_ta = RichTextField(verbose_name=_("Answer (Tamil)"), blank=True)

    question_te = models.TextField(
        verbose_name=_("Question (Telugu)"),
        blank=True)
    answer_te = RichTextField(verbose_name=_("Answer (Telugu)"), blank=True)

    question_kn = models.TextField(
        verbose_name=_("Question (Kannada)"),
        blank=True)
    answer_kn = RichTextField(verbose_name=_("Answer (Kannada)"), blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('Active'),
        help_text=_('Toggle to show/hide this FAQ')
    )

    def translate_text(self, text, target_lang):
        """Translates text only if it's not cached."""
        if not text:
            return ""

        cache_key = f"translation_{text}_{target_lang}"
        translation = cache.get(cache_key)
        # Cache for 1 day
        if not translation:
            translated_text = translator.translate(text, dest=target_lang).text
            cache.set(cache_key, translated_text, timeout=86400)
            translation = translated_text

        return translation

    def save(self, *args, **kwargs):
        """Auto-fill translations if not already set."""
        if self.question and self.answer:
            for lang_code in self.LANGUAGE_CHOICES.keys():
                question_field = f"question_{lang_code}"
                answer_field = f"answer_{lang_code}"

                if not getattr(self, question_field):
                    setattr(
                        self,
                        question_field,
                        self.translate_text(self.question, lang_code))

                if not getattr(self, answer_field):
                    setattr(
                        self,
                        answer_field,
                        self.translate_text(self.answer, lang_code))

        super().save(*args, **kwargs)

    def get_question(self, language='en'):
        """Return question in the selected language."""
        if language in self.LANGUAGE_CHOICES:
            return getattr(self, f'question_{language}', self.question)
        return self.question

    def get_answer(self, language='en'):
        """Return answer in the selected language."""
        if language in self.LANGUAGE_CHOICES:
            return getattr(self, f'answer_{language}', self.answer)
        return self.answer

    def __str__(self):
        return self.question
