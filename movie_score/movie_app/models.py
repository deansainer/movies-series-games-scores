from django.db import models


class MovieGenre(models.Model):
    genre = models.CharField(max_length=55)

    def __str__(self):
        return self.genre


class MovieScore(models.Model):
    score = models.FloatField(max_length=2)

    def __str__(self):
        return f'{self.score}'


class Movie(models.Model):
    name = models.CharField(max_length=55)
    release_date = models.IntegerField()
    genre = models.ForeignKey(MovieGenre, on_delete=models.CASCADE)
    score = models.ForeignKey(MovieScore, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class SeriesGenre(models.Model):
    genre = models.CharField(max_length=55)

    def __str__(self):
        return self.genre


class SeriesScore(models.Model):
    score = models.FloatField(max_length=2)

    def __str__(self):
        return f'{self.score}'


class Series(models.Model):
    name = models.CharField(max_length=55)
    release_date = models.IntegerField()
    genre = models.ForeignKey(MovieGenre, on_delete=models.CASCADE)
    score = models.ForeignKey(MovieScore, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class GameGenre(models.Model):
    genre = models.CharField(max_length=55)

    def __str__(self):
        return self.genre


class GameScore(models.Model):
    score = models.FloatField(max_length=2)

    def __str__(self):
        return f'{self.score}'


class Game(models.Model):
    name = models.CharField(max_length=55)
    release_date = models.IntegerField()
    genre = models.ForeignKey(MovieGenre, on_delete=models.CASCADE)
    score = models.ForeignKey(MovieScore, on_delete=models.CASCADE)

    def __str__(self):
        return self.name