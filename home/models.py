from django.db import models


class Card(models.Model):
    name = models.CharField(max_length=200)
    mana_cost = models.CharField(max_length=50, blank=True)
    cmc = models.FloatField(default=0)  # Converted Mana Cost
    type_line = models.CharField(max_length=200)
    oracle_text = models.TextField(blank=True)
    colors = models.CharField(max_length=50, blank=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.name


class CommanderDeck(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    cards = models.ManyToManyField(Card)

    def __str__(self):
        return self.name
    


