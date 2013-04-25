from django.db import models
from model_utils.models import TimeStampedModel

# Create your models here.
class Player(TimeStampedModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    wins = models.IntegerField(blank=True, default=0)
    losses = models.IntegerField(blank=True, default=0)
    curr_win_streak = models.IntegerField(blank=True, default=0)
    last_seen = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.nickname


class Battle(TimeStampedModel):
    attacker = models.ForeignKey('Player', related_name='attacker')
    defender = models.ForeignKey('Player', related_name='defender')
    winner = models.ForeignKey('Player', related_name='winner')
    start = models.DateTimeField(auto_now_add=True, blank=True)
    end = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return "%s v. %s" % (self.attacker, self.defender,)
