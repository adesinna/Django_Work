from django.db import models

# Create your models here.


class Club(models.Model):
    name = models.CharField(max_length=200)
    date_est = models.DateTimeField()
    stadium = models.CharField(max_length=200)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Coach(models.Model):
    name = models.CharField(max_length=100)
    club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True)
    date_birth = models.DateField()
    joined_date = models.DateField()
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=100)
    date_birth = models.DateField()
    joined_date = models.DateField()
    nationality = models.CharField(max_length=100)
    club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True)
    coach = models.ForeignKey(Coach, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Sponsor(models.Model):
    name = models.CharField(max_length=200)
    player = models.ManyToManyField(Player)  # many to many

    class SponsorIndustry(models.TextChoices):
        TEXTILE = "CO", 'Textile'
        BEVERAGES = 'BE', 'Beverages'
        TECH = 'TE', 'Tech'
        AVIATION = 'AV', "Aviation"
        FOOTBALL = 'FB', 'Football'

    industry = models.CharField(
        choices=SponsorIndustry.choices,
        default=SponsorIndustry.FOOTBALL,
        max_length=2
    )

    def __str__(self):
        return self.name



# salah.sponsor_set.all() thats how players see their sponsors
# sponsor.player since it is an attritube