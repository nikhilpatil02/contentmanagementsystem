from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_id = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    phone = models.IntegerField()
    pincode = models.IntegerField()
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    type_of_user = models.CharField(max_length=10, default="Author")