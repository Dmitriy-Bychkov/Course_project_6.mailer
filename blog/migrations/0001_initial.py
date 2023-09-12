# Generated by Django 4.2.4 on 2023-09-11 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='заголовок')),
                ('description', models.TextField(verbose_name='содержимое')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='изображение')),
                ('creation_date', models.DateTimeField(verbose_name='дата публикации')),
                ('views_count', models.IntegerField(default=0, verbose_name='количество просмотров')),
            ],
            options={
                'verbose_name': 'блог',
                'verbose_name_plural': 'статьи',
            },
        ),
    ]
