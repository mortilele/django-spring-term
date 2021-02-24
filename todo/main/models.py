from django.contrib.auth.models import User
from django.db import models


class ToDoGroup(models.Model):
    name = models.CharField(verbose_name='Название группы',
                            max_length=100)

    class Meta:
        verbose_name = 'Группа задач'
        verbose_name_plural = 'Группы задач'

    def __str__(self):
        return self.name


class ToDoItem(models.Model):
    IN_PROGRESS = 1
    DONE = 2

    STATUSES = (
        (IN_PROGRESS, 'В прогрессе'),
        (DONE, 'Закончено')
    )

    group = models.ForeignKey(ToDoGroup,
                              on_delete=models.CASCADE,
                              verbose_name='Группа задач',
                              related_name='todos')
    name = models.CharField(verbose_name='Название задачи',
                            max_length=100)
    created_at = models.DateTimeField(verbose_name='Дата создания',
                                      auto_now_add=True)
    due_date = models.DateTimeField(verbose_name='Дедлайн задачи',
                                    blank=True,
                                    null=True)
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              verbose_name='Владелец задачи')
    status = models.PositiveSmallIntegerField(verbose_name='Статус задачи',
                                              choices=STATUSES,
                                              default=IN_PROGRESS)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        indexes = [
            models.Index(fields=['owner', 'group', 'status'])
        ]
        ordering = ['-due_date']

    def __str__(self):
        return f'{self.name} - {self.owner}'
