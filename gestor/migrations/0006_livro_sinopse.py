# Generated by Django 5.0.4 on 2024-05-02 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0005_rename_quantidadedisponivel_livro_quantidade_disponivel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='sinopse',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
