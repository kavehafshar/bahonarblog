# Generated by Django 4.1.3 on 2022-11-26 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_alter_post_likes'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Token',
        ),
    ]
