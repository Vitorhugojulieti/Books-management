# Generated by Django 5.0.4 on 2024-05-02 21:12

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0002_alter_customuser_cpf_alter_customuser_telefone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_reserva', models.DateField(default=django.utils.timezone.now)),
                ('data_devolucao', models.DateField(blank=True, null=True)),
                ('devolvido', models.BooleanField(default=True, editable=False)),
                ('livros', models.ManyToManyField(to='gestor.livro')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]