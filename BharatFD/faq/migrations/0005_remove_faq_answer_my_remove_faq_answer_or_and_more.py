# Generated by Django 5.1.5 on 2025-02-02 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faq',
        '0004_faq_created_at_faq_updated_at_alter_faq_answer_or_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faq',
            name='answer_my',
        ),
        migrations.RemoveField(
            model_name='faq',
            name='answer_or',
        ),
        migrations.RemoveField(
            model_name='faq',
            name='answer_si',
        ),
        migrations.RemoveField(
            model_name='faq',
            name='question_my',
        ),
        migrations.RemoveField(
            model_name='faq',
            name='question_or',
        ),
        migrations.RemoveField(
            model_name='faq',
            name='question_si',
        ),
    ]
