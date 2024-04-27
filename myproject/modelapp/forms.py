import datetime

from django import forms


class registerform(forms.Form):
    firstname=forms.CharField(max_length=10,min_length=8)
    lastname=forms.CharField(max_length=10)
    phone_number=forms.IntegerField()
    email_id=forms.EmailField()
    password=forms.CharField(min_length=10,max_length=15)
    confirm_password=forms.CharField(min_length=10,max_length=15)



import datetime
class myform(forms.Form):
    Name=forms.CharField(min_length=5,max_length=15)
    salary=forms.IntegerField()
    email=forms.EmailField()
    height=forms.DecimalField(max_digits=5,decimal_places=3)
    terms=forms.BooleanField()
    # dob=forms.DateField(input_formats=["%Y-%m-%d"])
    #time=forms. TimeField(widget=datetime.datetime.now())
    Gender=forms.ChoiceField(choices=[("M","male"),("F","female")])
    specialize=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=[('ba','batsman'),('bba','bowler'),('ee','allrounder')])
    resume=forms.FileField()
    password=forms.CharField(min_length=8,max_length=16,  widget=forms.PasswordInput)
    review=forms.CharField(max_length=500,widget=forms.Textarea)
    websitelink=forms.URLField()
    image=forms.ImageField()
