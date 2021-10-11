# Generated by Django 3.2.8 on 2021-10-11 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_auto_20211011_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theme_label',
            name='nps',
        ),
        migrations.AddField(
            model_name='nps',
            name='theme_label',
            field=models.ManyToManyField(blank=True, related_name='theme_labels', to='feedback.Theme_label'),
        ),
    ]
