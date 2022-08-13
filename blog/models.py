from django.db import models

# Create your models here.
class About(models.Model):
    __tablename__ = "about"
    main_title = models.CharField(max_length=500)
    main_desc = models.TextField()
    sub_title = models.CharField(max_length=500)
    sub_desc = models.TextField()

class Team(models.Model):
    __tablename__ = "team"
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', default='images/team.jpg')

class Contact(models.Model):
    __tablename__ = "contact"
    desc = models.TextField()
    addr = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    webadr = models.CharField(max_length=200)
    contact_info = models.CharField(max_length=200)
    contact_info_desc = models.TextField()

class Plan(models.Model):
    __tablename__ = "plan"
    plan_type = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    account = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    space = models.CharField(max_length=50)
    support = models.CharField(max_length=50)

class Mails(models.Model):
    __tablename__ = "mails"

    name = models.CharField(max_length=100)
    sender = models.CharField(max_length=100)
    message = models.TextField()

class Emails:
    id:int
    name:str
    sender:str
    message:str