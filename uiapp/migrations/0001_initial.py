# Generated by Django 4.0.4 on 2022-05-05 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=70)),
                ('comment', models.TextField(max_length=2000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
