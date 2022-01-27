from django.db import models
import datetime
from django.utils import timezone
from datetime import timedelta


# Create your models here.


class allcourses(models.Model):
    coursename = models.CharField(max_length=500)
    instructorname = models.CharField(max_length=500)
    startedfrom = models.DateTimeField("started from")

    def publishedrecently(self):
        return self.startedfrom >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.coursename


class details(models.Model):
    course = models.ForeignKey(allcourses, on_delete=models.CASCADE)
    coursetype = models.CharField(max_length=500)
    yourchoice = models.BooleanField(default=False)

    def __str__(self):
        return self.coursetype
