# Generated by Django 2.2.1 on 2019-05-15 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='screenplay',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='screenplay', to='movies.Person'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='director', to='movies.Person'),
        ),
        migrations.CreateModel(
            name='PersonMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=128, null=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Person')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='starring',
            field=models.ManyToManyField(null=True, related_name='starring', through='movies.PersonMovie', to='movies.Person'),
        ),
    ]
