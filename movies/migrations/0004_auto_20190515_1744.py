# Generated by Django 2.2.1 on 2019-05-15 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20190515_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='starring',
            field=models.ManyToManyField(through='movies.PersonMovie', to='movies.Person'),
        ),
    ]
