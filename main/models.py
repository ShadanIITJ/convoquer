from django.db import models
from django.utils import timezone
class circket(models.Model):
    team1 = models.CharField(max_length=40)
    team2 = models.CharField(max_length=40)
    date_posted = models.DateTimeField(default = timezone.now)
    team1_score = models.CharField(max_length=30)
    team2_score = models.CharField(max_length=30)
    result = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.team1}'+ " vs " + f'{self.team2}'