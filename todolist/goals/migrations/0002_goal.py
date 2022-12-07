# Generated by Django 4.0.1 on 2022-12-07 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(verbose_name='Дата создания')),
                ('updated', models.DateTimeField(verbose_name='Дата последнего обновления')),
            ],
        ),
    ]