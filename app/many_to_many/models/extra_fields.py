from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=30)
    clubs = models.ManyToManyField(
        'Club', through='Career',
    )

    def __str__(self):
        return self.name

class Club(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Career(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True)

    def __str__(self):
        return '{player}, {club} ({start} - {end})'.format(
            player=self.player.name,
            club=self.club.name,
            start=self.start_year,
            end=f'{self.end_year}' if self.end_year else '',
        )