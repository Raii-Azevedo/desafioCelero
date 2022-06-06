from django.db import models
from django.conf import settings


class Base(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Athlete(Base):
    name = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="name", null=True,)
    sex = models.CharField(max_length=1)
    age = models.IntegerField()
    height = models.DecimalField(max_digits=3, decimal_places=1)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    team = models.CharField(max_length=50)
    noc = models.CharField(max_length=3)
    games = models.CharField(max_length=20)
    year = models.IntegerField()
    season = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    sport = models.CharField(max_length=20)
    event = models.CharField(max_length=20)
    medal = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Athlete'
        verbose_name_plural = 'Athletes'
        unique_together = ['name', 'age']

        def __str__(self):
            return f'{self.name}, age: {self.age} play for {self.team}'

