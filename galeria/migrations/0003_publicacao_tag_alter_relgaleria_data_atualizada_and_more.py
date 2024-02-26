# Generated by Django 5.0.1 on 2024-02-18 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0002_relgaleria'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacao',
            name='tag',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='relgaleria',
            name='data_atualizada',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='relgaleria',
            name='data_criada',
            field=models.DateTimeField(),
        ),
    ]
