from django.db import models
from django.contrib.postgres.fields import HStoreField,ArrayField,DateTimeRangeField,DateRangeField
from django.utils.translation import gettext as _
from django.utils import timezone
import datetime
# from django.db.models.functions import Now
from django.db import models
# Create your models here.
class First(models.Model):
    fname=models.CharField(max_length=200)
    date=DateRangeField(default=['2023-01-01', '2023-01-03'])
    class Meta:
        indexes=[models.Index(fields=['fname','date'])]

class Second(models.Model):
    fname=models.CharField(max_length=200)
    lname=models.CharField(max_length=100)
    def __str__(self):
        return self.fname
    
    class Meta:
        indexes=[models.Index(fields=['fname','lname'])]
        index_together=["fname","lname"]
from django.utils.timezone import now
class Third(models.Model):
    facility=models.CharField(max_length=200)
    people_in=models.IntegerField()
    people_out=models.IntegerField()
    recordated_at=models.DateTimeField(default=now)
    