from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

class Genre(models.Model):
    name = models.CharField(max_length=32)

class Movie(models.Model):
    title = models.CharField(max_length=128)
    director = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='director', null=True)
    screenplay = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='screenplay', null=True)
    starring = models.ManyToManyField(Person, through="PersonMovie", related_name='starring', null=True)
    year = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    genre = models.ManyToManyField(Genre)


class PersonMovie(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    role = models.CharField(max_length=128, null=True)
