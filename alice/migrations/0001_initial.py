# Generated by Django 4.2.1 on 2023-05-14 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request', models.CharField(max_length=250)),
                ('response', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]