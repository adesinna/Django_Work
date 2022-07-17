from django.db import models
from django.utils import timezone

# Create your models here.


class TaskStatus(models.TextChoices):
    PENDING = 'PE', 'Pending'
    COMPLETED = 'CO', 'Completed'
    DROPPED = 'DR', 'Dropped'


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now())
    deadline = models.DateTimeField(null=True, blank=True)  # it is an optional field that is why null is true
    status = models.CharField(
        choices=TaskStatus.choices,
        default=TaskStatus.PENDING,
        max_length=2
    )
    tag = models.ManyToManyField(Tag, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.content} - {self.get_status_display()}'  # it shows the full pending instead of PE
