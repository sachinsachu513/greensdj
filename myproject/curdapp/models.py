from django.db import models

# Create your models here.
from django.db import models
class employees1(models.Model):
    empno=models.IntegerField()
    empname=models.CharField(max_length=15)
    empsalary=models.IntegerField()
    empphno=models.IntegerField()
    empadress=models.CharField(max_length=15)
    email=models.EmailField()


    def __str__(self):
        return self.empname
