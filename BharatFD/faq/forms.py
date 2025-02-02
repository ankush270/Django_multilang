from django import forms
from .models import FAQ
from ckeditor.widgets import CKEditorWidget


class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Use the default CKEditor configuration
        self.fields['answer'].widget = CKEditorWidget(config_name='default')
        self.fields['answer_hi'].widget = CKEditorWidget(config_name='default')
        self.fields['answer_bn'].widget = CKEditorWidget(config_name='default')
        self.fields['answer_gu'].widget = CKEditorWidget(config_name='default')
        self.fields['answer_ta'].widget = CKEditorWidget(config_name='default')
        self.fields['answer_te'].widget = CKEditorWidget(config_name='default')
        self.fields['answer_kn'].widget = CKEditorWidget(config_name='default')
