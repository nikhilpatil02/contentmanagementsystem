from django.db import models
from user.models import Users

# Create your models here.
class Content(models.Model):
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=300)
    summary = models.CharField(max_length=60)
    #document = models.BinaryField()
    user = models.ForeignKey(Users,on_delete = models.CASCADE)

class Categories(models.Model):
    content = models.ForeignKey(Content, on_delete = models.CASCADE)
    category_name = models.CharField(max_length=30)