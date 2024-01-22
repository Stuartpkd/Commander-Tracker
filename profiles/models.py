from django.db import models
from django.contrib.auth.models import User
from home.models import Card
from django.db.models.signals import post_save
from django.dispatch import receiver


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SavedCard(models.Model):
    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.card.name} - {self.category.name}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    saved_cards = models.ManyToManyField(Card, through='SavedCard', blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
