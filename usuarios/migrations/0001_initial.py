# Generated by Django 4.0.3 on 2022-04-13 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_usuario', models.CharField(max_length=200)),
                ('email_usuario', models.EmailField(max_length=200)),
                ('password_usuario', models.CharField(max_length=200)),
                ('confirmacao_password_usuario', models.CharField(max_length=200)),
            ],
        ),
    ]
