# Generated by Django 2.1.5 on 2019-02-16 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_initial_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlepage',
            options={'ordering': ['-first_published_at'], 'verbose_name': 'Article'},
        ),
    ]