from django.db import models
from django.contrib.auth.models import User  # users

# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)  # it allows it to be blank
    complete = models.BooleanField(default=False)  # this allows the task to have a default of blank!
    created = models.DateTimeField(auto_now_add=True)  # create time and date when I create the object

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']  # Order it by the value complete when you list this task!
