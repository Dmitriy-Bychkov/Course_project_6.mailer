# Generated by Django 4.2.4 on 2023-09-09 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='frequency',
            field=models.CharField(choices=[('dayly', 'ежедневно'), ('weekly', 'еженедельно'), ('monthly', 'ежемесячно')], default='day', max_length=30, verbose_name='периодичность'),
        ),
    ]
