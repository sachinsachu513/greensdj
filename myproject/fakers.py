import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings" )

import django

django.setup()

from curdapp.models import employees1
from faker import Faker
from random import *

faker= Faker()

def fakeemployees():
    f_empid=randint(200,999)
    f_name=faker.name()
    f_salary=randint(40000,70000)
    f_phno=randint(6000000000,9999999999)
    f_address=faker.city()
    f_email=faker.email()
    emp= employees1.objects.get_or_create(empno=f_empid,empname=f_name,empsalary=f_salary,empphno=f_phno,empadress=f_address,email=f_email)



for i in range (0,10):
    fakeemployees()
