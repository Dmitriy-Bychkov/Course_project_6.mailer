# Generated by Django 4.2.4 on 2023-09-13 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0009_rename_owner_client_client_owner_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='client_owner',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='mailing',
            old_name='mailing_owner',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='message_owner',
            new_name='owner',
        ),
    ]
