from django.db import models

# Create your models here.
class Phone(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    os = models.CharField(max_length=10)


class ApplePhone(Phone):
    ios_version = models.CharField(max_length=10)


class AndroidPhone(Phone):
    android_version = models.CharField(max_length=10)


class HuaweiPhone(Phone):
    app_galery_version = models.CharField(max_length=10)
