from random import randint

from datetime import date
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver


def get_random_number():
    return randint(1, 100)


def age(birthday):
    if birthday is None:
        return ''

    today = date.today()
    if birthday > today:
        return 0
    else:
        return today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    birthday = models.DateField(null=True, blank=True)
    random_number = models.PositiveSmallIntegerField(default=get_random_number)

    @property
    def eligible(self):
        if self.birthday is None:
            return ''
        elif age(self.birthday) > 13:
            return 'allowed'
        else:
            return 'blocked'

    @property
    def bizz_fuzz(self):
        result = ''

        if self.random_number % 3 == 0:
            result += 'Bizz'
        if self.random_number % 5 == 0:
            result += 'Fuzz'

        if result != '':
            return result
        else:
            return self.random_number


# noinspection PyUnusedLocal
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# noinspection PyUnusedLocal
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
