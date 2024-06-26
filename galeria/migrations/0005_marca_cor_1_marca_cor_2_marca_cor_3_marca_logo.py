# Generated by Django 5.0.1 on 2024-02-18 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0004_publicacao_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='marca',
            name='cor_1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='marca',
            name='cor_2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='marca',
            name='cor_3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='marca',
            name='logo',
            field=models.URLField(blank=True, null=True),
        ),
    ]
