# Generated by Django 3.0.6 on 2020-06-19 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ex01', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tip',
            options={'permissions': (('can_downvote', 'can downvote'),)},
        ),
    ]
