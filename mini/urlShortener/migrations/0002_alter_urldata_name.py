# Generated by Django 4.1.5 on 2023-01-19 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlShortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urldata',
            name='name',
            field=models.CharField(max_length=300, null=True, unique=True),
        ),
    ]