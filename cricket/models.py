from django.db import models


class Team(models.Model):
    Team_name = models.CharField(max_length=20)
    caption = models.CharField(max_length=20)
    map_location = models.CharField(max_length=1200)

    def __str__(self):
        return str(self.Team_name) + ' - ' + str(self.map_location)


class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    bat_style = models.CharField(max_length=20)
    ball_style = models.CharField(max_length=20)

