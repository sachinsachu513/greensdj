from django.db import models

# Create your models here.
class employtable (models.Model):
    name=models.CharField(max_length=15)
    age=models.IntegerField()
    mailid=models.EmailField()
    phn=models.IntegerField()
    destination=models.CharField(max_length=10)

    def __str__(self):
        return self.name


class studenttable(models.Model):
    studentid=models.IntegerField()
    studentname=models.CharField(max_length=15)
    phonenumber=models.IntegerField()
    coursename=models.CharField(max_length=10)
    emailid=models.EmailField()
    doj=models.DateField()


    def __str__(self):
        return self.studentname

class database(models.Model):
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    phone_number=models.IntegerField()
    email_id=models.EmailField()
    password=models.CharField(max_length=7)
    confirm_password=models.CharField(max_length=7)



    def __str__(self):
       return self.firstname


