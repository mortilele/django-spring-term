from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import User, UserProfile


@receiver(post_save, sender=User)
def create_user_token(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
