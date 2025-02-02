from django.contrib import admin
from .models import FAQ
from ckeditor.widgets import CKEditorWidget
from django import forms


class FAQAdminForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply CKEditor widget for 'answer' and translation fields
        self.fields['answer'].widget = CKEditorWidget(config_name='default')
        self.fields['answer_hi'].widget = CKEditorWidget(config_name='default')
        self.fields['answer_bn'].widget = CKEditorWidget(config_name='default')
        self.fields['answer_gu'].widget = CKEditorWidget(config_name='default')
        self.fields['answer_ta'].widget = CKEditorWidget(config_name='default')
        self.fields['answer_te'].widget = CKEditorWidget(config_name='default')
        self.fields['answer_kn'].widget = CKEditorWidget(config_name='default')


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    form = FAQAdminForm
    list_display = ['question', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active']
    search_fields = ['question', 'answer']
    ordering = ['created_at']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        (None, {
            'fields': ('question', 'answer', 'is_active',
                       'created_at', 'updated_at'
                       )
        }),
        ('Translations', {
            'fields': (
                'question_hi', 'answer_hi',
                'question_bn', 'answer_bn',
                'question_gu', 'answer_gu',
                'question_ta', 'answer_ta',
                'question_te', 'answer_te',
                'question_kn', 'answer_kn',
            ),
            'classes': ('collapse',)
        }),
    )

    def save_model(self, request, obj, form, change):
        obj.save()
