from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length= 20)
    lastname = models.CharField(max_length= 20)
    email = models.CharField(max_length = 50)

    class meta:
        db_table  = 'tbluser'

class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length = 50)
    phone = models.IntegerField()
    date = models.DateField(max_length= 20)
    gender = models.CharField(max_length= 6)
    address = models.CharField(max_length= 50)
    message = models.CharField(max_length= 100)

class StaffList(models.Model):
    seqid  = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    appointment_id = models.ForeignKey(Appointment, on_delete = models.CASCADE)  
