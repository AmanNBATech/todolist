from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class todo(models.Model):
    task =models.CharField(max_length=222)
    task_date = models.DateTimeField()
    new = models.CharField(max_length=50,null=True)
    use= models.ForeignKey(User,on_delete=models.CASCADE,null=True)
   
    def __str__(self):
        return self.task
