# Generated by Django 3.0.6 on 2020-05-22 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ex04', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='homeworld',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ex04.Planets'),
        ),
    ]