from django.db import models
from django.utils.timezone import now

class Contestant(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Game(models.Model):
    name = models.CharField(max_length=255, unique=True)
    active = models.BooleanField(default=False)
    upvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Score(models.Model):
    contestant = models.ForeignKey(Contestant, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    score = models.FloatField()
    timestamp = models.DateTimeField(default=now)
