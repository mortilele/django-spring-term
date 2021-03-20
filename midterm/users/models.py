from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    SUPER_ADMIN = 1
    GUEST = 2

    ROLES = (
        (SUPER_ADMIN, 'Admin'),
        (GUEST, 'Guest')
    )

    role = models.PositiveSmallIntegerField(choices=ROLES, default=GUEST)

    def __str__(self):
        return f'{self.username} - {self.role}'


class UserProfile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='profile',
                                primary_key=True)
    address = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
