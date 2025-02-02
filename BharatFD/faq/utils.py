from django.core.cache import cache
from googletrans import Translator

translator = Translator()


def get_translation(text, target_lang):
    cache_key = f"translation_{text}_{target_lang}"
    translation = cache.get(cache_key)

    if not translation:
        translation = translator.translate(text, dest=target_lang).text
        cache.set(cache_key, translation, timeout=86400)
        # Cache for 1 day (86400 seconds)

    return translation
