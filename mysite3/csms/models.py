
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Customer(models.Model):
    ccode = models.CharField(max_length=10)
    cname = models.CharField(max_length=20)
    birth = models.IntegerField(max_length=12)
    phoneNum = models.CharField(max_length=15)
    address = models.CharField(max_length=60)
    imgfile = models.ImageField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(null=True, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.ccode+" "+self.cname+" "+str(self.birth)+" "+self.phoneNum+" "+self.address


class Service(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sNo = models.AutoField(primary_key=True)
    ccode = models.CharField(max_length=10)
    cname = models.CharField(max_length=20)
    sDate = models.DateTimeField(null=True, blank=True)
    departure = models.CharField(max_length=60)
    arrival = models.CharField(max_length=60)
    fee = models.IntegerField(max_length=10)
    type = models.CharField(max_length=10)
    imgfile = models.ImageField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(null=True, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()