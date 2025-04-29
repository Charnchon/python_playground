import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Donut(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    pub_date = models.DateTimeField("date published")

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Order(models.Model):
    donut = models.ForeignKey(Donut, on_delete=models.CASCADE)
    pub_date = models.DateTimeField("date published")