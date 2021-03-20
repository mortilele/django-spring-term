from django.conf import settings
from django.db import models


# Create your models here.


class BookJournalBase(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Book(BookJournalBase):
    num_pages = models.PositiveSmallIntegerField()
    genre = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


class Journal(BookJournalBase):
    BULLET = 1
    FOOD = 2
    TRAVEL = 3
    SPORT = 4

    TYPES = (
        (BULLET, 'Bullet'),
        (FOOD, 'Food'),
        (TRAVEL, 'Travel'),
        (SPORT, 'Sport'),
    )

    type = models.PositiveSmallIntegerField(choices=TYPES)
    publisher = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.PROTECT,
                                  related_name='journals')

    class Meta:
        verbose_name = 'Journal'
        verbose_name_plural = 'Journals'
